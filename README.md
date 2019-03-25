# Light Speed Engine

- 'Light Speed' acadamic paper information extraction
- Supporting sites:
  - [x] [Management Science](https://pubsonline.informs.org/journal/mnsc)

## TODO

- Test asynchronous HTTP requests (aiohttp)
- Data Storage in JSON files
- Add support to more sites
  - [Journal of Finance](https://onlinelibrary.wiley.com/loi/15406261)
  - [RFS]
  - [JFE]
  - [JFQA]

### Future Function(s):

- [ ] CLI support with `argparse`
- [ ] Re-Structure
  - async/coroutine request for same issue(multiple articles)
  - different magazine parsing (parse_ms(),..)
    - items
      - total articles?
      - article title
      - article authors
      - date
      - abstract
      - link
  - filesystem, make folders, and make/write dot md files
- [ ] Async web-scraping with Golang
- [ ] Mobile app support for both Android anad iOS ([Flutter](https://flutter.dev/))

## Version:

### v0.3

- Add support for fetch volume, issue list for Management Science
- Full support for Managment Science
- Full abstract for Management Science
- Add support for string volume, issue values
- Switch to `requests-html`

### v0.2

- Fix minor issues
- Get volumes from Volume 46-65

### v0.1

- Demo for Management Science
- With `requests` and `beautifulsoup4`
