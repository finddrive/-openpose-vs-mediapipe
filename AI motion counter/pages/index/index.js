// index.js
// 获取应用实例
const app = getApp()
var COS = require('../../utils/cos-wx-sdk-v5.js')


Page({
  data: {
    userInfo: {},
    hasUserInfo: false,
    canIUse: wx.canIUse('button.open-type.getUserInfo'),
    canIUseGetUserProfile: false,
    canIUseOpenData: wx.canIUse('open-data.type.userAvatarUrl') && wx.canIUse('open-data.type.userNickName'), // 如需尝试获取用户信息可改为false
    addimage: "/static/WXADD.jpg",
    select: false,
    tihouWay: "请选择运动",
    inputinfo: {"type": '', "vid_path":''},  //传入后端数据[cat, vid_path]
    countresult: {} //接收返回数据
  },
  // 事件处理函数
  bindViewTap() {
    wx.navigateTo({
      url: '../logs/logs'
    })
  },
  onLoad() {
    if (wx.getUserProfile) {
      this.setData({
        canIUseGetUserProfile: true
      })
    }
  },
  getUserProfile(e) {
    // 推荐使用wx.getUserProfile获取用户信息，开发者每次通过该接口获取用户个人信息均需用户确认，开发者妥善保管用户快速填写的头像昵称，避免重复弹窗
    wx.getUserProfile({
      desc: '展示用户信息', // 声明获取用户个人信息后的用途，后续会展示在弹窗中，请谨慎填写
      success: (res) => {
        console.log(res)
        this.setData({
          userInfo: res.userInfo,
          hasUserInfo: true
        })
      }
    })
  },
  getUserInfo(e) {
    // 不推荐使用getUserInfo获取用户信息，预计自2021年4月13日起，getUserInfo将不再弹出弹窗，并直接返回匿名的用户个人信息
    console.log(e)
    this.setData({
      userInfo: e.detail.userInfo,
      hasUserInfo: true
    })
  },
  
  bindShowMsg() {
    this.setData({
     select:!this.data.select
    })
  },
  //下拉框  
  //mySelect: (e) =>{
  mySelect:function(e){
   var name = e.currentTarget.dataset.name;
   let that = this
//    var ename
//    if (name == "跳绳"){  ename = 'jump rope'  }
//    if (name == "俯卧撑"){  ename = 'push ups'}
//    if (name == "引体向上"){  ename = 'pull ups'}
   that.setData({
    ['inputinfo.type']: name,
    tihouWay: name,
    select: false
   })
   console.log(that.data.inputinfo)
  },

  //上传视频
  uploadvideo(){
    wx.chooseMedia({
      count: 1,
      mediaType: ['video'],
      sourceType: ['camera'], //album'
      maxDuration: 60,
      camera: 'back',
      success: (res) => {
        let media = res.tempFiles[0]
        //console.log(media.size)
        console.log(media.thumbTempFilePath)
        let that = this
        if (media.size) {
          that.setData({
            addimage: media.thumbTempFilePath,
            ['inputinfo.vid_path']: media.tempFilePath
          })
          console.log(that.data.inputinfo.vid_path)
        }
      }
  })
},

  //点击按钮 请求后台
  counting(){
    //上传视频
    var up_vid = wx.getFileSystemManager().readFileSync(this.data.inputinfo.vid_path, "base64") //将视频进行base64编码。
    var dict = {} //当前结果
    wx.request({
      url: 'http://127.0.0.1:5000/uploadvid',
      header: {'content-type': "application/x-www-form-urlencoded",},
      data: {video: up_vid, info: this.data.inputinfo.type},
      method: 'POST',
      success: (res) => {
        console.log("上传成功",res.data)
        let that = this
        that.setData({
          countresult: res.data
        })
        dict = res.data
        dict["image"] = that.data.addimage
      },
      fail:(res) =>{
        wx.showToast({
          title: '计数失败',
          icon: 'fial',
          duration: 2000
         })
      },
      complete(){   
        console.log('complete') 
        wx.showModal({
          title: '是否保存此记录？',
          success: function (res) {
            if (res.confirm) {
              console.log('点击确定')//点击确定事件，放入本地

              //wx.removeStorageSync('localStorage')
              console.log("删除结果",wx.getStorageSync("localStorage"))
              if((wx.getStorageSync("localStorage")).length == 0){
                var curRecord =new Array()
                curRecord[0]=dict
              }else{
                var curRecord = wx.getStorageSync("localStorage")
                curRecord.unshift(dict) //新的在前面
              }
              console.log("存入内容",curRecord)
              wx.setStorageSync('localStorage', curRecord)  //date: count, date, type, image
            } else {
              console.log('点击取消')//点击取消事件
            }
            // that.setData({
            //   tihouWay: "请选择运动",
            //   addimage: "/static/WXADD.jpg",
            //   countresult: {} 
            // })
          }
        })
      }
    })
    
   },

});







  
