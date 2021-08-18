<template>
  <div class="footer-wrap">
    <span class="footer-content"
      >Made with <i class="fa fa-heart"></i> in San Francisco by
      <b>Coral</b></span
    >
    <div class="chat-icon">
      <i class="fa fa-comment-o"></i>
    </div>
  </div>
</template>

<style lang="scss">
.footer-wrap {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 15px 60px;
  min-height: 53px;
  background-color: #6cdcd4;
}
.footer-content {
  color: #fff;
  font-size: 14px;
}
.chat-icon {
  position: fixed;
  right: 30px;
  bottom: 30px;
  background-color: #fff;
  width: 80px;
  height: 80px;
  text-align: center;
  line-height: 80px;
  font-size: 38px;
  border-radius: 100%;
  box-shadow: 0 3px 0 rgba(0, 0, 0, 0.1);
}
</style>

<script>
export default {
  components: {},
  data() {
    return {};
  },
  computed: {},
  methods: {},
};
</script>