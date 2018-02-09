### 作用
用来修改文本文档里某些常常需要改动的项, 基于jinja2


### 测试
```
cd test
template -if test/test.md -of test/test1.md -v test/vars
```

### 用法
一个文档模板如下
```
>* 应聘职位：{{job}}
>* 居住地址: {{address}}
```


其中**应聘职位**和**居住地址**可能是要更改的


变量文件如下
```
{
"job": "xxx实习",
"address": "xxxx省xxxx市"
}
```
就是json格式


详细例子看test目录下
