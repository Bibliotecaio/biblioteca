angular.module('fbPage', [])
  
.directive('fbPage',
  function fbPage($rootScope, $window) {
    return {
      restrict: 'E',
      replace: true,
      scope: true,

      link: function (scope, elem, attrs) {
        if (!$window.FB) {
          // Load Facebook SDK
          $.getScript('//connect.facebook.net/en_US/sdk.js', function () {
            $window.FB.init({
              appId: $rootScope.facebookAppId,
              xfbml: true,
              version: 'v2.8'
            });
            renderLikeButton();
          });
        } else {
          renderLikeButton();
        }
        function renderLikeButton() {
          elem.html(
            `<div class="fb-page"
              data-href="https://www.facebook.com/%D0%9C%D1%83%D0%B7%D0%B5%D0%B9%D0%BD%D0%BE-%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D1%87%D0%BD%D0%BE-%D0%B0%D1%80%D1%85%D0%B8%D0%B2%D0%BD%D1%8B%D0%B9-%D0%BE%D1%82%D0%B4%D0%B5%D0%BB-726207747416733"
              data-width="450"
              data-hide-cover="false"
              data-show-facepile="false"
              data-show-posts="false">
            </div>
            <p>При реализации проекта используются средства государственной
              поддержки, выделенные в качестве гранта в соответствии c распоряжением
              Президента Российской Федерации №68-рп от 05.04.2016 и на основании
              конкурса, проведенного Общероссийской общественной организацией «Союз
              пенсионеров России».<br>
            </p>
          `);
          $window.FB.XFBML.parse(elem.parent()[0]);
        }
      }
    };
});
