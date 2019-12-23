<template>
    <div id=""></div>
</template>
 
<script>
  import axios from 'axios'
  export default {
    name: 'YunShuBigFileUpload',
    props: {
      fileId: { // 上传 type="file"的id
        type: String
      },
      UploadComplete: { // 完成时执行函数
        type: Function
      },
      ChunkSize: { // 切片大小  单位时MB
        type: Number
      },
      url: { //上传地址
        type: String
      },
      md5: { // 文件的md5值
        type: String
      },
      UploadProgress: { // 上传进度
        type: Function
      }
    },
    watch: {
      md5() {
        this.myMd5 = this.md5
      }
    },
    data() {
      return {
        uploadFile: {
          chunk: 0,
          isLastChunk: false,//是否最后一片文件
          fileName: ''//文件名称
        },
        myMd5: '',
      }
    },
    created() {
      this.myMd5 = this.md5
    },
    methods: {
      chunksFile() {
        // this.fileId : '上传的input元素id'   例如 #input-file-upload
        let file = document.querySelector(this.fileId).files[0], //需要上传的文件
          chunkLength = 0; //文件分片后的长度
        this.uploadFile.fileName = file.name;
        if (file.size > 1024 * 1024 * this.ChunkSize) {
          chunkLength = Math.ceil(file.size / (1024 * 1024 * this.ChunkSize));
        } else {
          chunkLength = 1
        }
        this.uploadFile.chunk === chunkLength - 1 ? this.uploadFile.isLastChunk = true : false;
        let fm = new FormData();
        fm.append('md5', this.myMd5);
        fm.append('size', file.size);
        fm.append('chunk', this.uploadFile.chunk);
        fm.append('chunks ', chunkLength);
        fm.append('fileName ', this.uploadFile.fileName);
        fm.append('file', file.slice(this.uploadFile.chunk * 1024 * 1024 * this.ChunkSize, (this.uploadFile.chunk + 1) * 1024 * 1024 * this.ChunkSize));
        //通过ajax上传分片文件内容
        axios.post(this.url, fm).then((res) => {
          if (res.status == 200) {
            //上传成功，分片加一，上传下一片文件
            this.uploadFile.chunk++
            //上传完最后一片后传输结束
            const pr = parseInt((this.uploadFile.chunk + 1) / chunkLength * 100)
            this.UploadProgress(pr)
            if (this.uploadFile.isLastChunk) {
              this.UploadComplete()
            } else {
              //递归调用上传下一片
              this.chunksFile();
            }
          }
        }).catch((error) => {
          console.log(error)
            this.$Message.warning('上传失败!')
        });
      }
    }
  }
</script>
 
<style>
</style>