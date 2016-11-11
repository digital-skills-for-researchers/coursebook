# Digital Skills for Researchers: Coursebook

The live version of this coursebook can be viewed [here](http://digital-skills-for-researchers.github.io/coursebook/)




## Theme

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


