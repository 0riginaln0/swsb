It is what it is.

`./bombardier -c 250 -n 10000000 http://localhost:8080`

```
Go

  Statistics        Avg      Stdev        Max
  Reqs/sec    221801.48   19056.72  282195.84
  Latency        1.12ms   284.86us    39.26ms
  HTTP codes:
    1xx - 0, 2xx - 10000000, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    38.94MB/s


Lua 5.4 Astra runtime

  Statistics        Avg      Stdev        Max
  Reqs/sec     58399.78    2121.72   79024.64
  Latency        4.28ms   203.08us    32.64ms
  HTTP codes:
    1xx - 0, 2xx - 10000000, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    10.25MB/s


Java

  Statistics        Avg      Stdev        Max
  Reqs/sec     27436.38    1645.12   45772.56
  Latency        9.11ms    19.34ms      2.00s
  HTTP codes:
    1xx - 0, 2xx - 9999955, 3xx - 0, 4xx - 0, 5xx - 0
    others - 45
  Errors:
    dial tcp 127.0.0.1:8080: i/o timeout - 45
  Throughput:     4.82MB/s


Gleam

  Statistics        Avg      Stdev        Max
  Reqs/sec     15010.40    5071.78   26381.78
  Latency       16.66ms     7.84ms   180.91ms
  HTTP codes:
    1xx - 0, 2xx - 7872062, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     2.39MB/s


Python

  Statistics        Avg      Stdev        Max
  Reqs/sec      7439.38    2479.53   14046.72
  Latency       33.61ms   328.22ms     10.04s
  HTTP codes:
    1xx - 0, 2xx - 2734248, 3xx - 0, 4xx - 0, 5xx - 0
    others - 4836
  Errors:
       timeout - 4836
  Throughput:     1.43MB/s
```
