# Light Speed Engine

## Supporting sites:

|   Journal    |                                       Website                                       |    Latest Issue     |
| :----------: | :---------------------------------------------------------------------------------: | ------------------: |
|  [JF](/JF)   |                [site](https://onlinelibrary.wiley.com/loi/15406261)                 |  Volume 74, Issue 3 |
| [JFE](/JFE/) | [site](https://www.sciencedirect.com/journal/journal-of-financial-economics/issues) | Volume 133, Issue 2 |
| [RFS](/RFS)  |                     [site](https://academic.oup.com/rfs/issue)                      |  Volume 32, Issue 7 |
|  [MS](/MS)   |                 [site](https://pubsonline.informs.org/journal/mnsc)                 |  Volume 65, Issue 6 |

## TODO

- JFE Issue 20 problem [link](https://www.sciencedirect.com/journal/journal-of-financial-economics/vol/20/suppl/C)
- [JFQA](https://www.cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/all-issues)
  - click view all
  - save source code only html
  - PROBLEM! cloudflare protection
  - MS no requirement for issuelist (to be fixed)

### Future Function(s):

- CLI support with `argparse`
- Check if all issue is in the folder
- Asynchronous HTTP requests (`asyncio`, `aiohttp`)

### Future plans

- Seperate data from function
- Format for each journal and issuelink store seperately as CONSTANT
- Random picked paper for fun

### JSON format

#### Issue content format
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

#### Issue link format
```json
{
    "vol_num": {
        "1": {
            "date":"",
            "page":"",
            "link":"http://"
        }
    }
}
```

```python
# how to access link
issuelink['vol_num']['iss_num']['link']
```


## Version:

### v0.5

- Support JF, RFS
- Convert single journal json to markdown files as whole

### v0.4

- Supporting JFE
- Save as json files
- json to markdown converter

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
