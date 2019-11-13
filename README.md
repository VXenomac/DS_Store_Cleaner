# DS_Store_Cleaner
`DS_Store_Cleaner`是可以删除当前目录或指定目录下所有的 `.DS_Store` 文件的工具。 / `DS_Store_Cleaner` can delete all `.DS_Store` files in the current directory or in the specified directory.

## 什么是 .DS_Store？ / What is a .DS_Store?

`.DS_Store` 是 `macOS` 用来保存如何展示文件/文件夹的数据文件，如果开发/设计人员将 `.DS_Store` 文件上传或部署到线上环境，可能造成文件目录结构泄露，特别是备份文件、源代码文件。如果不设置 `.gitignore` 文件，`.DS_Store` 很容易被上传到 `Github` 之上，可以使用该工具删除已经上传的文件。

[ds_store_exp](https://github.com/lijiejie/ds_store_exp) 就是这样的一个 `.DS_Store` 文件泄露利用脚本。

`.DS_Store` is the data file used by `macOS` to describe files/folders. If the developer/designer uploads or deploys the `.DS_Store` file to the production environment, the file directory structure may be leaked, especially the source code file.If you don't set the `.gitignore` file, `.DS_Store` can easily be uploaded to `Github`. Then you can use `DS_Store_Cleaner` tool to delete these files that have already been uploaded.

[ds_store_exp](https://github.com/lijiejie/ds_store_exp) is such a `.DS_Store` file leak exploit script.

## 使用方法 / Usage

* 清除当前路径下所有 `.DS_Store` 文件 / Clear all `.DS_Store` files in the current directory：

```python
python DS_Store_Cleaner
```

* 清除指定路径下所有 `.DS_Store` 文件 / Clear all `.DS_Store` files in the specified directory：

```python
python DS_Store_Cleaner.py ~/Desktop
```

## Licnese

[MIT License](https://github.com/VXenomac/DS_Store_Cleaner/blob/master/LICENSE)