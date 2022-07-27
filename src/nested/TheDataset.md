# The Genesis/Mountain Dataset

The <> Dataset is a Bittensor’s current language modeling dataset consisting of a set of smaller datasets combined together. Currently, it contains 1500 GiB of unlabeled text.

Servers in Bittensor are valdiated by for their ability to understand the text contained in the <> Dataset. To do this, Validators querey Servers who must produce embeddings and token prdecitons in response. Scores derived from these responses determine the incentives Servers see, thus guiding the network to understand the dataset better. 

## Storage

In order to ensure global access and make the network robust to single points of failure, Genesis is stored on The InterPlanetary File System [(IPFS)](https://docs.ipfs.io/concepts/what-is-ipfs/#what-is-ipfs) as a set of small chunks, files no larger than 1Mb, each containing a small sample of the larger dataset. These small chunks are organized into a set of 22 datasets each with a standard data format, for instance, Arxiv articles or Github code.

## Quereying <>

Every file on Genesis can be accessed via its unique hash. These can be queried directly using a tool like Curl and the hash of the file.  For instance, we can query an individual file like so.

Command:
```bash
curl -X POST "http://ipfs.opentensor.ai/api/v0/object/get?arg=Qme2dawBzozFGtKWX73fh5fmB8NJD7TRS2XSWKhJB4WbJd"
```
Output:
```LaTeX
"Data": Right now, American protest music sounds like\nthis.\n...we don’t believe you, cuz we the people...\n...a million dollar loan.
...
```

## <> Orginization

Genesis is organized under the following hash:
```bash
QmXL3fiJUBtpn7zSN3FVnS2spZoe4N1c1aCRatn773qPFZ
```

```bash
curl -X POST "http://ipfs.opentensor.ai/api/v0/object/get?arg=QmXL3fiJUBtpn7zSN3FVnS2spZoe4N1c1aCRatn773qPFZ"
```



```bash
curl -X POST "http://ipfs.opentensor.ai/api/v0/object/get?arg=QmUzpNL94qN7RFYUkeji2ZGgDDiWALM1MXwu74RNmcov6Q
```

```LaTeX
"Name": "01-YoutubeSubtitles-5899.txt" 
"Hash": "QmSj7mzxdDw8gd8rqqzijCDxsUs8YRi6EsJtRWiLsHA9Ce", 
"Size": 5173 

"Name": "01-YoutubeSubtitles-59.txt\", 
"Hash": "Qme2dawBzozFGtKWX73fh5fmB8NJD7TRS2XSWKhJB4WbJd", 
"Size": 885 

"Name": "01-YoutubeSubtitles-590.txt\"
"Hash": "QmUSzQgkamYWVhv938nbQgPrQz7CNfpmiUaF36z6Nx6Uzz", 
"Size": 6710 
...
```


