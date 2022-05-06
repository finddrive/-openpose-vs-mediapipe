// app.js
App({
  onLaunch() {
    // 展示本地存储能力
    const logs = wx.getStorageSync('logs') || []
    logs.unshift(Date.now())
    wx.setStorageSync('logs', logs)

    // 登录
    wx.login({
      success: res => {
        // 发送 res.code 到后台换取 openId, sessionKey, unionId
      }
    })

    if (!wx.cloud){
      console.error("请使用云")
    }else{
      wx.cloud.init({
        env:'prod-4g9l72fld70b682e',
        traceUser: true,
      })
    }
  },
  globalData: {
    userInfo: null,
    vid_path: null  //原始视频
  }
})
