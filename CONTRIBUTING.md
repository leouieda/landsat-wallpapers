# Contributing Guide

:tada: **First off, thank you for considering contributing to our project!** :tada:

These are some of the many ways to contribute:

* 🙏🏽: Request a wallpaper
* 🐛: Report or fix an error/typo/bug
* 🖼️: Contribute a new wallpaper (see below)

For wallpaper requests 🙏🏽 and bug reports 🐛, open an [Issue on
GitHub](https://github.com/leouieda/landsat-wallpapers/issues/new/choose).
Please select the appropriate category if you can.

## Contributing a wallpaper

New wallpapers are welcome through pull requests on GitHub. To do so, please
follow these steps (assuming that you're familiar with git/GitHub):

1. Fork the repository
1. Create a new branch (avoid sending PRs from your "main" branch)
1. Copy one of the notebooks in `code` to use as a template and rename it to
   the same name as your wallpaper file
1. File names should be all lowercase and separated by `-` (special characters
   are allowed)
1. Download the Level 2 (full scene `.tar` file) and Level 1 (only band 8 and
   the `MTL.txt` files) data for your wallpaper from
   [EarthExplorer](https://earthexplorer.usgs.gov/)
1. Place the `.tar` archive in the `code` folder
1. Place the band 8 and `MTL.txt` files in a subfolder of `code`
1. Neither of the above should be committed to the repository (there is a
   `.gitignore` rule that should prevent this)
1. Edit the first cell of the notebook to briefly describe your wallpaper
1. Copy the code to generate the cropped versions of the scene to a new cell
   and edit it to fit your target area
1. Ideally, the cropped scene should have at least 1000 pixels in easting in
   the panchromatic band and be roughly 16:9 in ratio
1. Edit the cells below to generate a nice looking image
1. Make sure to set the folder name in `data` and the prefix for the wallpapers
   to be the same as the notebook title
1. When you're satisfied with the wallpaper, make the first cell that crops the
   original scene into a Markdown cell (for future reference)
1. Rerun the notebook from top to bottom sequentially (use "Restart and run all
   cells")
1. Add a new section to the bottom of the README with your wallpaper (copy an
   entry and replace the name of your wallpaper)
1. Make sure you commit: the new data files in `data/yourfoldername`, the
   notebook in `code`, the `README.md` changes, and the 4k and 720p versions of
   the wallpapers in `wallpapers`
1. Open a pull request and wait for a review
