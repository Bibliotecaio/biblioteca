angular.module('documentLink', [
])
  
.directive('documentLink',
  function documentLink(ENV) {
    return {
      restrict: 'E',
      replace: true,
      transclude: true,
      scope: {
        fileId: '@'
      },
      template: '<a href="{{fileUrl}}" download ng-transclude></a>',
      link: function (scope, elem, attrs) {
        
        scope.$watch(function () {
          return [attrs.fileId];
        }, function() {
            scope.fileUrl = `${ ENV.fileStorageEndpoint }/${ attrs.fileId }`;
          },
          true
        );
        
      }
    };
});
