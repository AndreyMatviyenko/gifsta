$(document).ready(function () {

  $(document).on('mouseover', '.section--related .gifplayer', (function () {
      var src = replaceToGif($(this).attr("src")),
          spinner = $(this).parent().find('.spinner');
      if ($(this).attr('data-loaded') != 1) {
          $(this).attr('data-loaded', 1);
          var preloadedImg = new Image();
          preloadedImg.alt = '';
          preloadedImg.src = src;
          
          preloadedImg.onload = function() {
            var div = document.createElement('img');
            $('body').append($(div).attr({"src": src}).hide());
            // $('body').append($(div).attr({"src": src}).hide());
            spinner.css('visibility', 'hidden');
          }
      }
      $(this).attr("src", src);
  }));

  $(document).on('mouseout', '.section--related .gifplayer', (function() {
      var src = replaceToJpg($(this).attr("src"));
        $(this).attr("src", src);
  }));

  function replaceToGif(str) {
      return str.replace(/\.jpg$/, '.gif');
  }
  function replaceToJpg(str) {
      return str.replace(/\.gif$/, '.jpg');
  }

  //arrow to top
  if ($('.back-to-top').length) {
    var scrollTrigger = 100,
        // px
    backToTop = function () {
      var scrollTop = $(window).scrollTop();
      if (scrollTop > scrollTrigger) {
        $('.back-to-top').addClass('show');
      } else {
        $('.back-to-top').removeClass('show');
      }
    };
    backToTop();
    $(window).on('scroll', function () {
      backToTop();
    });
    $('.back-to-top').on('click', function (e) {
      e.preventDefault();
      $('html,body').animate({
        scrollTop: 0
      }, 700);
    });
  }

  var shareTitle = document.title;
  var btnShareUrl = window.location.href;

  $(document).on("click", ".share_gif li", function (event) {
    event.preventDefault();
    var type = $(this).data('share');
    var id = $(this).parent().data('gif-id');
    shareGif(type, id);
  });

  function shareGif(type, id) {
    switch (type) {
      case 'facebook':
        href = 'https://www.facebook.com/sharer/sharer.php?u=' + btnShareUrl;
        return !window.open(href, 'Facebook', 'width=640,height=300');
        break;
      case 'twitter':
        href = 'http://twitter.com/intent/tweet?text=' + shareTitle + '&url=' + btnShareUrl;
        return !window.open(href, 'Twitter', 'width=640,height=300');
        break;
      case 'whatsapp':
        href = 'whatsapp://send?text=' + shareTitle + '%0A' + btnShareUrl;
        return !window.open(href, 'WhatsApp', 'width=640,height=300');
        break;
      case 'vkontakte':
        href = 'https://vk.com/share.php?url=' + btnShareUrl;
        return !window.open(href, 'Vkontakte', 'width=640,height=300');
        break;
      default:
        console.log("url");
    }
  }

  $("body").on("click", ".search-icon", function () {
    $(this).toggleClass("on");
    $(".main-header .search-form").slideToggle();
  });

  $("body").on("click", ".select-wrap", function () {
    $(this).toggleClass("on");
  });

  //SVG Fallback
  if (!Modernizr.svg) {
    $("img[src*='svg']").attr("src", function () {
      return $(this).attr("src").replace(".svg", ".png");
    });
  };

  $("img, a").on("dragstart", function (event) {
    event.preventDefault();
  });
});

function secondsToTime(seconds) {
  let d = Number(seconds);
  let h = Math.floor(d / 3600);
  let m = Math.floor(d % 3600 / 60);
  let s = Math.floor(d % 3600 % 60);
  return (h > 0 ? h + ':' : '') + (m > 0 ? (h > 0 && m < 10 ? '0' : '') + m + ':' : '0:') + (s < 10 ? '0' : '') + s;
}

Vue.config.debug = true;

Vue.component('gif-player', {
  template: '#gif-player',
  created() {
    this.isGif = !!this.src.match(/.gif$/);
    this.isVideo = !!this.src.match(/(.mp4)$/);
  },
  ready() {
    this.$e = $(this.$el);
    this.$video = this.$e.find('video');
    this.video = this.$video.get(0);

    if (this.video) {
      this.video.addEventListener('loadedmetadata', () => {
        this.durationSeconds = this.video.duration;
      });

      this.video.addEventListener('timeupdate', () => {
        this.currentSeconds = this.video.currentTime;
      });
    }
  },
  data() {
    return {
      durationSeconds: 0,
      currentSeconds: 0,
      isGif: false,
      isVideo: false
    };
  },
  props: {
    loop: String,
    controls: String,
    src: String,
    href: String
  },
  methods: {
    play() {
      this.video.play();
    },
    pause() {
      this.video.pause();
    },
    reset() {
      this.video.currentTime = 0;
      this.pause();
    },
    hover() {
      console.log('hover');
    }
  },
  computed: {
    currentTime() {
      return secondsToTime(this.currentSeconds);
    },
    durationTime() {
      return secondsToTime(this.durationSeconds);
    },
    progress() {
      return (this.currentSeconds / this.durationSeconds).toFixed(2);
    }
  }
});

new Vue({
  el: 'body'
});