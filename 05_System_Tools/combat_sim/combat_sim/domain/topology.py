"""Abstract Zone Topologies, Zone Profiles, Environmental Traits, and Graph Routing."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Set

from combat_sim.core.types import CoverType, Difficulty, ZoneTraitType


@dataclass
class ZoneProfile:
    """Environmental check profile for hazard tests and searches within a zone."""
    difficulty: Difficulty = Difficulty.NORMAL
    tn: int = 1
    description: str = ""

    @property
    def shorthand(self) -> str:
        """Visual shorthand code, e.g. '5+/1', '4+/2', '6/1'."""
        return f"{self.difficulty.label}/{self.tn}"


@dataclass
class ZoneTrait:
    """An environmental trait or hazard attached to a zone."""
    trait_type: ZoneTraitType
    description: str = ""
    is_active: bool = True
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Zone:
    """An abstract tactical zone node in an encounter topology."""
    id: str
    name: str
    profile: ZoneProfile = field(default_factory=ZoneProfile)
    cover: CoverType = CoverType.NONE
    traits: List[ZoneTrait] = field(default_factory=list)
    loot_bulk: int = 0
    is_flammable: bool = True
    is_burning: bool = False
    is_blocked: bool = False
    directional_cover: Dict[str, CoverType] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def has_trait(self, trait_type: ZoneTraitType) -> bool:
        """Check if zone currently has an active trait of the specified type."""
        return any(t.trait_type == trait_type and t.is_active for t in self.traits)

    def get_trait(self, trait_type: ZoneTraitType) -> Optional[ZoneTrait]:
        """Retrieve the active trait object of the specified type, if present."""
        for t in self.traits:
            if t.trait_type == trait_type and t.is_active:
                return t
        return None

    def add_trait(self, trait: ZoneTrait) -> None:
        """Attach a new environmental trait to the zone."""
        # Replace if same type exists
        self.traits = [t for t in self.traits if t.trait_type != trait.trait_type]
        self.traits.append(trait)
        if trait.trait_type == ZoneTraitType.BURNING:
            self.is_burning = True

    def remove_trait(self, trait_type: ZoneTraitType) -> bool:
        """Remove a trait by type. Returns True if removed."""
        initial_len = len(self.traits)
        self.traits = [t for t in self.traits if t.trait_type != trait_type]
        if trait_type == ZoneTraitType.BURNING:
            self.is_burning = False
        return len(self.traits) < initial_len

    def get_cover_from(self, source_zone_id: Optional[str] = None) -> CoverType:
        """Get cover classification relative to an incoming attack source zone."""
        if source_zone_id and source_zone_id in self.directional_cover:
            return self.directional_cover[source_zone_id]
        return self.cover

    def set_directional_cover(self, from_zone_id: str, cover: CoverType) -> None:
        """Assign directional cover granted against attacks originating from a specific zone."""
        self.directional_cover[from_zone_id] = cover


@dataclass
class TopologyGraph:
    """Graph structure managing zone connectivity, distance routing, and pathfinding."""
    zones: Dict[str, Zone] = field(default_factory=dict)
    adjacency: Dict[str, Set[str]] = field(default_factory=dict)

    def add_zone(self, zone: Zone) -> None:
        """Register a zone in the topology graph."""
        self.zones[zone.id] = zone
        if zone.id not in self.adjacency:
            self.adjacency[zone.id] = set()

    def connect(self, z1: str, z2: str, bidirectional: bool = True) -> None:
        """Establish adjacency between two zones."""
        if z1 not in self.zones or z2 not in self.zones:
            raise KeyError(f"Both zones must exist before connecting: {z1}, {z2}")
        self.adjacency.setdefault(z1, set()).add(z2)
        if bidirectional:
            self.adjacency.setdefault(z2, set()).add(z1)

    def disconnect(self, z1: str, z2: str, bidirectional: bool = True) -> None:
        """Remove adjacency connection between two zones (e.g. collapsed tunnel/shoring)."""
        if z1 in self.adjacency:
            self.adjacency[z1].discard(z2)
        if bidirectional and z2 in self.adjacency:
            self.adjacency[z2].discard(z1)

    def get_zone(self, zone_id: str) -> Optional[Zone]:
        """Look up a zone by its identifier."""
        return self.zones.get(zone_id)

    def get_adjacent(self, zone_id: str) -> List[str]:
        """Return list of accessible adjacent zone IDs."""
        return sorted(list(self.adjacency.get(zone_id, set())))

    def are_adjacent(self, z1: str, z2: str) -> bool:
        """Check if two zones share a direct boundary."""
        return z2 in self.adjacency.get(z1, set())

    def get_distance(self, z1: str, z2: str) -> int:
        """Calculate shortest distance (zone hops) between two zones using BFS.
        
        Returns:
            int: Number of zone transitions (0 if same zone, -1 if unreachable).
        """
        if z1 == z2:
            return 0
        if z1 not in self.zones or z2 not in self.zones:
            return -1

        visited: Set[str] = {z1}
        queue: deque[tuple[str, int]] = deque([(z1, 0)])

        while queue:
            curr, dist = queue.popleft()
            for neighbor in self.adjacency.get(curr, set()):
                if neighbor == z2:
                    return dist + 1
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))

        return -1  # Unreachable

    def find_path(self, z1: str, z2: str) -> List[str]:
        """Compute shortest path of zone IDs from z1 to z2 inclusive using BFS."""
        if z1 == z2:
            return [z1]
        if z1 not in self.zones or z2 not in self.zones:
            return []

        visited: Set[str] = {z1}
        queue: deque[list[str]] = deque([[z1]])

        while queue:
            path = queue.popleft()
            curr = path[-1]
            for neighbor in self.adjacency.get(curr, set()):
                if neighbor == z2:
                    return path + [neighbor]
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(path + [neighbor])

        return []

    def get_zones_within_distance(self, zone_id: str, max_dist: int) -> List[str]:
        """Find all zone IDs reachable within max_dist hops."""
        if zone_id not in self.zones or max_dist < 0:
            return []

        visited: Dict[str, int] = {zone_id: 0}
        queue: deque[tuple[str, int]] = deque([(zone_id, 0)])

        while queue:
            curr, dist = queue.popleft()
            if dist < max_dist:
                for neighbor in self.adjacency.get(curr, set()):
                    if neighbor not in visited:
                        visited[neighbor] = dist + 1
                        queue.append((neighbor, dist + 1))

        return sorted(list(visited.keys()))
