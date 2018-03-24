angular.module('documentCover', [
])
  
.directive('documentCover',
  function documentCover(ENV, localStorageService,) {
    return {
      restrict: 'E',
      replace: true,
      scope: {
        imgId: '@',
        alt: '@',
        title: '@',
        imgHeight: '@'
      },
      template: '<img ng-src="{{coverImageUrl}}" alt="{{alt}}" title="{{title}}"/>',
      link: function (scope, elem, attrs) {
        
        scope.$watch(function () {
          return [attrs.imgId, attrs.imgHeight];
        }, function() {
            scope.coverImageUrl = `${ ENV.fileStorageEndpoint }/${ attrs.imgId }?height=${ attrs.imgHeight }`;

          },
          true
        );
        
      }
    };
});
