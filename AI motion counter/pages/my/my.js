// pages/home/home.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
      recordList:[],  //历史记录
      select: {type:false, date:false},
      shift: {type: "运动类型", date: "日期"}, //下拉框
      showtype:""
  },

    /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    
},


  bindShowType() {
    this.setData({
     "select.type":!this.data.select['type']
    })
    console.log(this.data.select['type'])
  },
  //下拉框  
  typeSelect:function(e){
   var name = e.currentTarget.dataset.name;
   let that = this
   var ename
   if (name == " "){  
       that.setData({
           ['shift.type'] : "运动类型",
           "select.type":!that.data.select['type']
        })
   }else{
        if (name == "跳绳"){  ename = 'jump rope'  }
        if (name == "俯卧撑"){  ename = 'push ups'}
        if (name == "引体向上"){  ename = 'pull ups'}
        if (name == "深蹲"){  ename = 'squat'}
        if (name == "单臂举重"){  ename = 'weight lifting'}
        that.setData({
            showtype: ename,
            ['shift.type']: name,
            "select.type":!that.data.select['type']
        })
        console.log(this.data.select['type'])
    }
   //console.log(that.data.inputinfo)
  },

bindDateChange: function(e) {
    this.setData({
        "shift.date": e.detail.value
    })
},


bindShowDate() {
    this.setData({
     "select.date":!this.data.select['date']
    })
    console.log(this.data.select['date'])
  },

dateSelect:function(e){
    let that = this
    that.setData({
        "shift.date" : "日期",
        "select.date":!that.data.select['date']
        })
    console.log(this.data.select['date'])
},



  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
     
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
   //本地storage中取值
   var curres = wx.getStorageSync('localStorage')
   this.setData({
     recordList: curres
   })
   console.log("当前数据",this.data.recordList)
    
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})