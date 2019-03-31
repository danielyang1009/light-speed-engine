# Light Speed Engine

- 'Light Speed' acadamic paper information extraction
- Supporting sites:
  - [x] [MS](https://pubsonline.informs.org/journal/mnsc)
  - [x] [JFE](https://www.sciencedirect.com/journal/journal-of-financial-economics/issues)

## TODO

- JFE Issue 20 problem [link](https://www.sciencedirect.com/journal/journal-of-financial-economics/vol/20/suppl/C)
- Add support to more sites
  - [Journal of Finance](https://onlinelibrary.wiley.com/loi/15406261)
  - [RFS]
  - [JFQA]

### Future Function(s):

- CLI support with `argparse`
- Asynchronous HTTP requests (`asyncio`, `aiohttp`)

### JSON format

```json
{
    "journal": "",
    "volume": "",
    "issue": "",
    "date": "",
    "page": "",
    "article": [
        {
            "no": "",
            "title": "",
            "date": "",
            "author": [],
            "abstract": "",
            "link": ""
        }
    ]
}
```



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
