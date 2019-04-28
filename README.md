## S3-latency

<p align="center"><img width="100" src="https://upload.wikimedia.org/wikipedia/commons/9/93/Amazon_Web_Services_Logo.svg" />
<img width="100" src="https://img.stackshare.io/service/25/amazon-s3.png" />
</p>

Benchmark `PUT`, `DELETE`, `GET` command for `1KB, 10KB, 1MB, 10MB` size files in each regions in `AWS S3`.
Each result shows Average latency Time for 10 times.

```python
# each regions benchmark
regions = ['us-east-2', 'us-east-1',
           'us-west-1', 'us-west-2',
           'ap-south-1',
           'ap-northeast-2', 'ap-northeast-1',
           'ap-southeast-1', 'ap-southeast-2', 
           'ca-central-1','eu-central-1',
           'eu-west-1', 'eu-west-2',
           'eu-west-3',
           'eu-north-1', 'sa-east-1',
]

# file sizes benchmark
files = ['1KB', '10KB', '1MB', '10MB']
```



#### Quick Start

create credentials file on your local machine.

```shell
$ mkdir ~/.aws
$ vim ~/.aws/credentials
```

```
[default]
aws_access_key_id=<your access key>
aws_secret_access_key=<your secret access key>
```

```shell
$ python3 s3_run.py
```



## Benchmark

From Korea(Seoul) Region(`ap-northeast-2c`) to Each Regions. Please see [s3.log](s3.log) file.

```
-----[ us-east-2 ]-----
File Size 1KB
	Average PUT latency 0.3934691905975341
	Average GET latency 0.1972438097000122
	Average DEL latency 0.2035255908966064
File Size 10KB
	Average PUT latency 0.3975818157196045
	Average GET latency 0.1948685884475708
	Average DEL latency 0.2000956773757934
File Size 1MB
	Average PUT latency 1.2001072883605957
	Average GET latency 0.4190945386886596
	Average DEL latency 0.2002393484115600
File Size 10MB
	Average PUT latency 4.0208817958831790
	Average GET latency 1.7918375253677368
	Average DEL latency 0.2052211523056030

-----[ us-east-1 ]-----
File Size 1KB
	Average PUT latency 0.4202607393264770
	Average GET latency 0.2105414152145385
	Average DEL latency 0.2145504236221313
File Size 10KB
	Average PUT latency 0.4343791246414185
	Average GET latency 0.2087876081466674
	Average DEL latency 0.2243231773376464
File Size 1MB
	Average PUT latency 0.8038835763931275
	Average GET latency 0.4241857290267944
	Average DEL latency 0.2423960924148559
File Size 10MB
	Average PUT latency 6.1047015428543090
	Average GET latency 1.4990855216979981
	Average DEL latency 0.2113099098205566

-----[ us-west-1 ]-----
File Size 1KB
	Average PUT latency 0.3146688699722290
	Average GET latency 0.1507223844528198
	Average DEL latency 0.1551310062408447
File Size 10KB
	Average PUT latency 0.3182317018508911
	Average GET latency 0.1526724815368652
	Average DEL latency 0.1610818862915039
File Size 1MB
	Average PUT latency 0.6638113975524902
	Average GET latency 0.2524497985839843
	Average DEL latency 0.1589655160903930
File Size 10MB
	Average PUT latency 3.3569829702377320
	Average GET latency 1.4616475582122803
	Average DEL latency 0.1625203132629394

-----[ us-west-2 ]-----
File Size 1KB
	Average PUT latency 0.2923774003982544
	Average GET latency 0.1528093338012695
	Average DEL latency 0.1962181329727172
File Size 10KB
	Average PUT latency 0.3794935941696167
	Average GET latency 0.1460643053054809
	Average DEL latency 0.1463476419448852
File Size 1MB
	Average PUT latency 0.6234967708587646
	Average GET latency 0.2793298959732055
	Average DEL latency 0.1518289327621459
File Size 10MB
	Average PUT latency 3.5462617635726930
	Average GET latency 1.6089293479919433
	Average DEL latency 0.1488687515258789

-----[ ap-south-1 ]-----
File Size 1KB
	Average PUT latency 0.3367386579513550
	Average GET latency 0.1691524982452392
	Average DEL latency 0.1732125282287597
File Size 10KB
	Average PUT latency 0.3526116371154785
	Average GET latency 0.1703629255294799
	Average DEL latency 0.1776876926422119
File Size 1MB
	Average PUT latency 0.6177640438079834
	Average GET latency 0.3034507989883422
	Average DEL latency 0.1767824649810791
File Size 10MB
	Average PUT latency 3.3337445020675660
	Average GET latency 1.4171964406967164
	Average DEL latency 0.1709996700286865

-----[ ap-northeast-2 ]-----
File Size 1KB
	Average PUT latency 0.0294530868530273
	Average GET latency 0.0110424041748046
	Average DEL latency 0.0115904092788696
File Size 10KB
	Average PUT latency 0.0252262830734252
	Average GET latency 0.0116529941558837
	Average DEL latency 0.0134159564971923
File Size 1MB
	Average PUT latency 0.0621462583541870
	Average GET latency 0.0210981130599975
	Average DEL latency 0.0113916635513305
File Size 10MB
	Average PUT latency 0.1882711410522461
	Average GET latency 0.1137933731079101
	Average DEL latency 0.0110766410827636

-----[ ap-southeast-1 ]-----
File Size 1KB
	Average PUT latency 0.2306092739105224
	Average GET latency 0.1097543239593505
	Average DEL latency 0.1190116405487060
File Size 10KB
	Average PUT latency 0.2407874584197998
	Average GET latency 0.1104554414749145
	Average DEL latency 0.1217018365859985
File Size 1MB
	Average PUT latency 0.4902917623519897
	Average GET latency 0.2345633983612060
	Average DEL latency 0.1171665430068969
File Size 10MB
	Average PUT latency 2.7003178834915160
	Average GET latency 1.1865426063537599
	Average DEL latency 0.1173614263534545

-----[ ap-southeast-2 ]-----
File Size 1KB
	Average PUT latency 0.3510033130645752
	Average GET latency 0.1709885358810424
	Average DEL latency 0.1830531358718872
File Size 10KB
	Average PUT latency 0.3592378854751586
	Average GET latency 0.1710273027420044
	Average DEL latency 0.1790776968002319
File Size 1MB
	Average PUT latency 0.7034335851669311
	Average GET latency 0.3531969785690307
	Average DEL latency 0.1798280715942382
File Size 10MB
	Average PUT latency 3.4303051710128782
	Average GET latency 1.4138346910476685
	Average DEL latency 0.1899488925933838

-----[ ap-northeast-1 ]-----
File Size 1KB
	Average PUT latency 0.1190845251083374
	Average GET latency 0.0528791427612304
	Average DEL latency 0.0612649202346801
File Size 10KB
	Average PUT latency 0.1330645561218261
	Average GET latency 0.0483139276504516
	Average DEL latency 0.0690757751464843
File Size 1MB
	Average PUT latency 0.3132515907287597
	Average GET latency 0.1246066808700561
	Average DEL latency 0.0630329847335815
File Size 10MB
	Average PUT latency 1.5392013311386108
	Average GET latency 0.7525208711624145
	Average DEL latency 0.0665940046310424

-----[ ca-central-1 ]-----
File Size 1KB
	Average PUT latency 0.4277769804000854
	Average GET latency 0.1969282627105713
	Average DEL latency 0.2043543338775634
File Size 10KB
	Average PUT latency 0.4046813011169433
	Average GET latency 0.1961323738098144
	Average DEL latency 0.2074999094009399
File Size 1MB
	Average PUT latency 0.7044886112213135
	Average GET latency 0.3544960737228393
	Average DEL latency 0.2008390903472900
File Size 10MB
	Average PUT latency 3.5950159311294554
	Average GET latency 1.6017854452133178
	Average DEL latency 0.2058943986892700

-----[ eu-central-1 ]-----
File Size 1KB
	Average PUT latency 0.5644833564758300
	Average GET latency 0.2821964025497436
	Average DEL latency 0.2850435018539429
File Size 10KB
	Average PUT latency 0.5786470651626587
	Average GET latency 0.2805391311645507
	Average DEL latency 0.2861155033111572
File Size 1MB
	Average PUT latency 1.0089457511901856
	Average GET latency 0.5901510953903198
	Average DEL latency 0.2875846624374389
File Size 10MB
	Average PUT latency 4.2058208465576170
	Average GET latency 2.3608003139495850
	Average DEL latency 0.2882647752761841

-----[ eu-west-1 ]-----
File Size 1KB
	Average PUT latency 0.5467856407165528
	Average GET latency 0.2696810007095337
	Average DEL latency 0.2710706710815430
File Size 10KB
	Average PUT latency 0.5664828538894653
	Average GET latency 0.2772149324417114
	Average DEL latency 0.2690214395523071
File Size 1MB
	Average PUT latency 1.0283177375793457
	Average GET latency 0.4448684453964233
	Average DEL latency 0.2726919412612915
File Size 10MB
	Average PUT latency 4.8126481056213380
	Average GET latency 1.9654175758361816
	Average DEL latency 0.2703055381774902

-----[ eu-west-2 ]-----
File Size 1KB
	Average PUT latency 0.5435325860977173
	Average GET latency 0.2731415271759033
	Average DEL latency 0.2733743429183960
File Size 10KB
	Average PUT latency 0.5490349054336547
	Average GET latency 0.2752829074859619
	Average DEL latency 0.2775721788406372
File Size 1MB
	Average PUT latency 0.9688710451126099
	Average GET latency 0.4915812492370605
	Average DEL latency 0.2744291543960571
File Size 10MB
	Average PUT latency 3.8903452634811400
	Average GET latency 2.9383730173110960
	Average DEL latency 0.2752056598663330

-----[ eu-west-3 ]-----
File Size 1KB
	Average PUT latency 0.5460410356521607
	Average GET latency 0.2736373186111450
	Average DEL latency 0.2759330511093140
File Size 10KB
	Average PUT latency 0.5469071149826050
	Average GET latency 0.3266200542449951
	Average DEL latency 0.2739025831222534

File Size 1MB
	Average PUT latency 0.9664048433303833
	Average GET latency 1.3283938646316529
	Average DEL latency 0.2740131378173828
File Size 10MB
	Average PUT latency 3.9636361360549928
	Average GET latency 2.9346849679946900
	Average DEL latency 0.2729789018630981

-----[ eu-north-1 ]-----
File Size 1KB
	Average PUT latency 0.6006274700164795
	Average GET latency 0.3024726152420044
	Average DEL latency 0.3028710365295410
File Size 10KB
	Average PUT latency 0.5996861934661866
	Average GET latency 0.3018431663513183
	Average DEL latency 0.3023591756820679
File Size 1MB
	Average PUT latency 1.0242538928985596
	Average GET latency 0.6004209995269776
	Average DEL latency 0.3014988660812377
File Size 10MB
	Average PUT latency 3.9297783851623533
	Average GET latency 3.1529757976531982
	Average DEL latency 0.3016827106475830

-----[ sa-east-1 ]-----
File Size 1KB
	Average PUT latency 0.6446306943893433
	Average GET latency 0.3196903705596924
	Average DEL latency 0.3323929786682129
File Size 10KB
	Average PUT latency 0.6504593610763549
	Average GET latency 0.3214278459548950
	Average DEL latency 0.3301063060760498
File Size 1MB
	Average PUT latency 0.9852907180786132
	Average GET latency 0.5091957092285156
	Average DEL latency 0.3293693065643310
File Size 10MB
	Average PUT latency 4.3386932849884040
	Average GET latency 2.3129598855972290
	Average DEL latency 0.3316281557083130
```



## Requirement

- Python 3.5+
- boto3 >= 1.9.134
- botocore >= 1.12.134



## Author

- Tae Hwan Jung(Jeff Jung) @graykode
- Author Email : [nlkey2022@gmail.com](mailto:nlkey2022@gmail.com)
