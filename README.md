# rpmbuild
rpmbuild
## 20211027 ops,ops.1.1.1,rpmbuild三個檔案壓縮後，可以放在原資料夾，拷貝過去後再判斷是否有該檔案，有的話就不解壓縮。不執行。
關鍵程式:
```
if [ ! -d "/myfolder" ]; then
mkdir /myfolder
fi
```
## 20211026
rpmbuild是給linux下載找後安裝用的，似乎有套件可以直接生成，但我忘了在那，也沒有找到，就先將會的放上來。
自動化 打包的開始，雖然還很沒有頭緒，但想到什麼就做什麼吧!!
