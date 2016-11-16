# Digital Skills for Researchers: Coursebook

The live version of this coursebook can be viewed [here](http://digital-skills-for-researchers.github.io/coursebook/)

ReadMe Contents:

- [Using the coursebook](#using-the-coursebook)
  - [Using our version](#using-our-version)
  - [Hosting your own version](#hosting-your-own-version)

- [Modifying the coursebook](#modifying-the-coursebook)
  - [Taking a copy](#taking-a-copy)
  - [Editing on GitHub](#editing-on-github)
  - [Editing on your desktop](#editing-on-your-desktop)
  - [Modifying content](#modifying-the-content)
  - [Modifying the theme](#modifying-the-theme)

- [Reporting Problems](#reporting-problems)
- [Contributions](#contributions)
- [Community](#community)
- [License](#license)



---

## Using the coursebook

You may use this coursebook either by directing students to the live version hosted on GitHub [here](http://digital-skills-for-researchers.github.io/coursebook/), or by taking a copy of the coursebook code and hosting your own version either on GitHub or on a private web server.

Instructions for both methods are included below.

### Using our version
You may use the coursebook in its current form by directing your students to the live version of the coursebook published [here](http://digital-skills-for-researchers.github.io/coursebook/). This version of the coursebook is subject to change, as it is automatically generated from the code hosted in this repository.

The live site is hosted using the GitHub Pages service, and will be online as long as the project code is also hosted on GitHub.


### Hosting your own version
You are also free to make a copy of the coursebook and host it either on GitHub or on your own web server. Follow the instructions in [Modifying the Coursebook](#modifying-the-coursebook) to take a copy of your own. You can then choose to modify the content (or not) as you choose.


---


## Modifying the coursebook

Follow these instructions if you wish to use the coursebook but also want to:

1. Ensure the content does not change unexpectedly OR
2. Make changes to the content OR
3. Make changes to the theme


### Step 1: Take a copy

Once you have a copy of the coursebook forked to your own GitHub account, you can make changes either through GitHub, or by downloading the code and making the changes using a desktop code editor.

[&raquo; Full instructions for taking a copy](#taking-a-copy)


### Step 2: Editing on GitHub

For **simple changes**, using GitHub is probably suitable. For more **extensive changes**, using a desktop editor is recommended.

[&raquo; Full instructions for editing on GitHub](#editing-with-github)


### Step 3: Editing on your desktop (optional)

If you plan to make regular or extensive changes to the coursebook, you may wish to run a copy of it on your desktop for editing purposes. You can then send the changes back to GitHub when you are happy with the result. This editing method requires some additional setup and technical knowledge.

[&raquo; Full instructions for editing on your desktop](#editing-with-desktop)


**Note:**<br>
It is **not recommended** to mix both methods of editing unless you are familiar with Git and GitHub, as merging the changes from multiple editing methods is not always straightforward.




---


### Taking a copy

You **must** do these steps before you can make any changes to the coursebook.


1. **Get a GitHub account**<br>
You will need a GitHub account where you can store your copy of the coursebook.

2. **Fork the coursebook**<br>
In GitHub when you "fork" it means "make a copy". Click the "Fork" button at the very top of this page on GitHub. Once you have forked the coursebook to your own account, your version will not pick up any changes made to our version (unless you tell it to).

3. **Check it is running**<br>
In a web browser, navigate to `https://[your-username].github.io/coursebook`, replacing `[your-username]` with your GitHub username. A live version of your coursebook copy should be visible at this address.



---


### Editing on GitHub

To make basic changes, you can use GitHub's built-in editor.

1. **Find the file you want to edit**<br>
First, make sure you are in _your_ copy, not our copy! Each coursebook page has a corresponding text file. Use the GitHub file view to find the file you wish to edit. All content pages are stored under the `modules` folder, except for the home page which is in the top level and called `index.md`.

2. **Edit the file**<br>
Once you have found and opened the file in GitHub, click the "Edit this file" button, which is a small pencil icon at the top right of the file's contents. Clicking the edit button will open the text editor, where you can make changes using Markdown syntax.

3. **Save your changes**<br>
After you have made your changes, click the green "Commit changes" button at the bottom of the editor. This will save your changes to the file.

4. **Preview the changes**<br>
Open your copy of the coursebook at `https://[your-username].github.io/coursebook` and check that your changes are now live. The live version may take up to 10 minutes to update, but usually takes less than 1 minute.



---



### Editing on your desktop


To make changes and preview them before publishing, you can download and edit the coursebook on your desktop.

As initial setup, you will need to download and install the following:

1. **Ruby**<br>
This is a programming language. You do not need to use it directly, but Jekyll needs it installed to be able to run. Installing Ruby can sometimes be a bit tricky if unexpected things go wrong. Allow time for this process, and don't feel bad about asking a techie for help. Instructions are available for [Windows][windows-ruby], [Mac][mac-ruby] and [Linux][ubuntu-ruby].


[windows-ruby]: http://rubyinstaller.org/
[mac-ruby]: https://optionalbits.com/tips-and-tricks-setting-up-ruby-on-os-x-89f353455736#.jrghzmfem
[ubuntu-ruby]: https://www.digitalocean.com/community/tutorials/how-to-install-ruby-on-rails-on-ubuntu-14-04-using-rvm

2. **Jekyll**<br>
This is the program which combines your content and theme files to produce a website. It runs automatically on GitHub, but you'll need to install it on your own computer to preview your work. Instructions are available [here][jekyll-install].

[jekyll-install]: https://jekyllrb.com/docs/installation/#install-with-rubygems

3. **Visual Studio Code**<br>
This is a free code editor which runs on any computer. You can use an alternative code editor if you like, but these instructions will assume you are using VS Code. You can download the installer from [here][vscode-install].

[vscode-install]: https://code.visualstudio.com

4. **GitKraken desktop app**<br>
This is the program you will use to connect to the GitHub website. This desktop app will allow you to pull code from GitHub to your desktop, and send changes from your desktop back to GitHub. Available for Windows, Mac and Linux from [here][gitkraken-download].

[gitkraken-download]: https://www.gitkraken.com/

5. **Coursebook code**<br>
Open up the GitKraken app and sign in to your GitHub account. Follow the instructions to "clone" the coursebook to your computer. This will create a folder on your computer which contains all the coursebook files. You can then edit these using a code editor.


Each time you wish to preview the coursebook and/or make changes you will need to:

1. **Open the coursebook in Visual Studio Code**<br>
Run the VS Code program, then in the top menu choose `File` > `Open Folder...` and select the coursebook folder.

2. **Run the coursebook preview**<br>
In VS Code, in the top menu choose `View` > `Integrated Terminal`. Click in the console window and type `jekyll serve` then press Enter. The web server will start up, and will tell you that the site is running. You can view the site in your web browser at the address `http://0.0.0.0:8080/coursebook`.


3. **Make changes to the coursebook**<br>
You can now make changes to the site files using VS Code. Each time you save a file, the site will be regenerated. Click the Refresh button in your browser to view the changes.

4. **Save changes back to GitHub**<br>
In GitKraken, at the top right click the green button "Stage all changes". In the bottom right Commit Message, type in a message describing your change, then click the green button "Commit". At the top-middle press the white up arrow to "Push" the changes to GitHub.


---

## Content

_**Note:** Modifying the coursebook **content** requires that you are comfortable formatting text content using [Markdown](markdown-syntax) rather than a text editor. Markdown is fairly simple to pick up, so don't be afraid to give it a go!_

_As an example, this page you're reading is written in Markdown, which you can view [here](README.md). The Markdown is then automatically converted into HTML headings, paragraphs, lists and links by GitHub._

[markdown-syntax]: https://daringfireball.net/projects/markdown/syntax



---


## Theme

_**Note:** Modifying the coursebook **theme** requires that you are comfortable working with **HTML and CSS** code. The coursebook is developed using [Jekyll](jekyll-site), which runs in the background on GitHub and combines the content with the theme to produce a static HTML/CSS website._

[jekyll-site]: https://jekyllrb.com/

The course content and the theme are kept separate. You do not need to change anything in the theme folder, unless you want to change the layout, colours, or add functionality such as additional JavaScript.

The theme and the content are automatically combined into a website by Jekyll, which is supported by GitHub.

To edit the theme you will need to be comfortable with HTML and CSS. You will also need to take some time to understand how the files are split up and how Jekyll inserts dynamic content into the HTML.

All code related to the display of the course can be found inside the `theme` folder.

```
theme
    _includes
        foot.html
        footer.html
        head.html
        sidebar.html
    _layouts
        page.html
    _sass
        layout.scss
        sidebar.scss
        typography.scss
        variables.scss
    assets
        styles.scss
```

### Layouts

A "layout" file contains HTML code for how a page should look. Within the HTML there are places where Jekyll can insert various pieces of content. These dynamic parts of a layout are surrounded by `{` curly brackets `}`.

This courseware currently uses only one page layout, called "page".

At the top of every content file, eg. `my-page.md` you can set the page layout in the "front matter" section:

```
---
title: My Page
layout: page
---
```

Currently, all pages have their layout set to `page`. If you create a new layout in the layouts folder, you can apply the layout to a page by changing the `layout` setting in the page's front matter.

You can read more about [Front Matter][front-matter] on the [Jekyll][jekyll] site.


[front-matter]: https://jekyllrb.com/docs/frontmatter/
[jekyll]: https://jekyllrb.com


### Includes

An "include" file contains a piece of layout which has a specific purpose. Using includes allows code to be split up into smaller pieces, making it easier to find and modify.

The includes used in this site are as follows:

- **head**
  Contains the HTML code which goes at the very top of an HTML page. This is where the site metadata is set, and where CSS files are imported.

- **sidebar**
  Contains the code for the sidebar menu. The links which are displayed on the sidebar are automatically created from the list in `_data/modules.yml`. To add or remove links from the sidebar, edit `modules.yml`.

- **footer**
  Contains the footer content such as licensing information and links which should be at the bottom of every page.

- **foot**
  Contains the HTML code which goes at the very bottom of an HTML page. This is where JavaScript files are imported.


### SASS

SASS is a form of CSS which has a bit more functionality included, such as variables, functions, and nested CSS. Using SASS also allows us to split up CSS across separate files.

Each file in the `_sass` folder contains CSS code for the appearance of a specific aspect of the site, as follows:

- **variables**
  Contains some variables for common design choices such as font and colour. Changing variables here will update the CSS code wherever those variables are used.

- **typography**
  Contains CSS for styling most things related to the display of text on the site. Covers the styles for headings, paragraphs, links etc.

- **layout**
  Contains CSS for styling most things related to the layout of the website. Covers the styles for the sidebar, footer, content sections etc.

- **sidebar**
  Contains CSS for styling the sidebar and its toggle button (which is only visible on mobile).

Each of these SASS files is then combined into a single CSS file thanks to `assets/styles.scss`.

If you add a new `.scss` file to the `_sass` folder, make sure to also import that new file in `styles.scss`.



## Community

You can find us on [Slack](https://digi-research-skills.slack.com/)!

Email one of the team to request an invite:

- Fabiana Kubke [f.kubke@auckland.ac.nz](mailto:"f.kubke@auckland.ac.nz")
- Tanya Gray [t.gray@aucklanduni.ac.nz](mailto:"t.gray@aucklanduni.ac.nz")





## Contributions

To submit changes or corrections please:

- Fork this project
- Make and commit the correction
- Submit a pull request

If you have many changes to submit please:

- Fork this project
- **Create a branch** for each logical grouping of changes
- Make and commit the corrections
- Submit a separate pull request for each branch / change

Please keep pull requests small to help us merge your suggestions more efficiently.




## Attributions

Logo Credit: [Crash Test Dummy](https://thenounproject.com/term/crash-test-dummy/4954/) by Wes Breazell on The Noun Project


