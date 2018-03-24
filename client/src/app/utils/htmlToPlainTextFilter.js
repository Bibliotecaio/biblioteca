angular.module('htmlToPlainTextFilter', [
])
  
.filter('htmlToPlainText', function htmlToPlainTextFilter() {
    return function(text) {
      return text ? String(text).replace(/<[^>]+>/gm, '') : '';
    };
  }
);