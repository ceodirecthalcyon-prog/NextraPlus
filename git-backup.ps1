param([string]$msg = "Auto backup")

# Go to project folder
Set-Location "E:\NextraPlus"

# Stage files
git add .

# Commit with timestamp
$time = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
git commit -m "$msg - $time"

# Push to GitHub
git push origin main
