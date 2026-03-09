param (
    [Parameter(Mandatory=$true)]
    [string]$Url,
    
    [Parameter(Mandatory=$false)]
    [string]$Title
)

if ($Title) {
    Write-Host "Downloading $Title from $Url ..."
    anyflip-downloader -title "$Title" $Url
} else {
    Write-Host "Downloading from $Url ..."
    anyflip-downloader $Url
}

Write-Host "Download complete!"
