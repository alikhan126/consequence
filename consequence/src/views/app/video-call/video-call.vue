<template>
  <div v-if="!getLoading">
    <div class="video-call-wrap">
      <div class="video-call-inner">
        <div class="row align-items-center">
          <div class="col-md-8">
            <div class="video-wrap">
              <div class="video-control">
                <img src="@/assets/images/products/headphone-1.jpg" alt />
                <div class="video-option">
                  <div class="option-top">
                    <i class="fa fa-ellipsis-v"></i>
                  </div>
                  <div class="option-bottom">
                    <div class="horizontal-menu-icon">
                      <i class="fa fa-ellipsis-h"></i>
                    </div>
                    <div class="icon-border">
                      <i class="fa fa-microphone"></i>
                      <i class="fa fa-video-camera"></i>
                    </div>
                    <div class="icon-border">
                      <i class="fa fa-user-o"></i>
                    </div>
                  </div>
                </div>
              </div>
              <div class="audio-video-option">
                <i class="fa fa-check-square-o"></i>
                <span>Check your audio and video</span>
              </div>
            </div>
          </div>
          <div class="col-md-4">
            <div class="video-content text-center">
              <h3>Ready to join?</h3>
              <div class="video-option mb-2">
                <b-button variant="primary" class="btn-radius mr-2"
                  >Ask to join</b-button
                >
                <b-button variant="link"
                  ><i class="fa fa-caret-square-o-left"></i>
                  <span>Present</span></b-button
                >
              </div>
              <b-button variant="link" class="text-primary casting-btn"
                ><i class="fa fa-play-circle-o"></i>
                <span>Cast this meeting</span></b-button
              >
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <Loader v-else />
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import Loader from "../../../components/loader/loader";
export default {
  props: {
    msg: String,
  },
  computed: {
    ...mapGetters(["getLoading"]),
  },
  mounted() {
    this.setLoading(true);
    setTimeout(() => {
      this.setLoading(false);
    }, 2000);
  },
  methods: {
    ...mapActions(["setLoading"]),
  },
  components: { Loader },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.video-call-wrap {
  max-width: 1170px;
  padding: 50px 0;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0 auto;
}
.video-call-wrap img,
.video-call-wrap video {
  border-radius: 20px;
  overflow: hidden;
  width: 100%;
  object-fit: cover;
  height: 450px;
}
.video-call-inner {
  width: 100%;
}
.video-content h3 {
  font-weight: 700;
  font-size: 26px;
  margin-bottom: 15px;
  margin-top: 0;
}
.video-option .btn-link {
  color: #999;
}
.video-option .btn-link:hover,
.casting-btn:hover {
  text-decoration: none;
}
.video-option .btn-link i {
  font-size: 16px;
  vertical-align: middle;
  margin-right: 5px;
}
.video-option .btn-link span {
  vertical-align: middle;
  line-height: 20px;
}
.casting-btn i {
  margin-right: 5px;
}
.audio-video-option {
  border: 1px solid #d0d0d0;
  margin-top: 20px;
  display: inline-block;
  padding: 3px 10px;
  cursor: pointer;
  border-radius: 20px;
}
.video-control {
  position: relative;
  overflow: hidden;
  border-radius: 20px;
}
.option-top {
  position: absolute;
  right: 30px;
  top: 25px;
  font-size: 20px;
  color: #fff;
  cursor: pointer;
}
.option-bottom {
  position: absolute;
  left: 0;
  bottom: 0px;
  font-size: 20px;
  right: 0;
  padding: 50px 15px 15px 30px;
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  background: -moz-linear-gradient(
    top,
    rgba(0, 0, 0, 0) 0%,
    rgba(0, 0, 0, 0.7) 100%
  ); /* FF3.6-15 */
  background: -webkit-linear-gradient(
    top,
    rgba(0, 0, 0, 0) 0%,
    rgba(0, 0, 0, 0.7) 100%
  ); /* Chrome10-25,Safari5.1-6 */
  background: linear-gradient(
    to bottom,
    rgba(0, 0, 0, 0) 0%,
    rgba(0, 0, 0, 0.7) 100%
  ); /* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */
  filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#00000000', endColorstr='#4a000000',GradientType=0 ); /* IE6-9 */
}
.horizontal-menu-icon i {
  font-size: 20px;
  color: #6cdcd4;
  cursor: pointer;
  vertical-align: bottom;
}
.icon-border i {
  color: #fff;
  width: 50px;
  height: 50px;
  border: 1px solid #fff;
  border-radius: 100%;
  text-align: center;
  line-height: 48px;
  cursor: pointer;
}
.icon-border i + i {
  margin-left: 15px;
}
.switch-account {
  display: flex;
  justify-content: flex-end;
}
.account-info span {
  color: #000;
  font-size: 12px;
  display: block;
  line-height: normal;
  text-align: right;
}
.account-img img {
  margin-left: 10px;
  width: 30px;
  height: 30px;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
  object-fit: cover;
  border-radius: 100%;
}
</style>
