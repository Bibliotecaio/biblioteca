angular.module('pageTitleService', [
])

.service('pageTitleService',
  function pageTitleService($rootScope, $state) {
    
    this._constructTitle = function (title) {
      let suffix = '| Biblioteca.io';

      if ($state.current.name.indexOf('admin') >= 0) {
        return `${ title } | Администрирование ${ suffix }`;
      }
      return `${ title } ${ suffix }`;
    };
      
    this._simpleTitle = function() {
      if (!$state.current.hasOwnProperty('data')){
        return;
      }
      
      let data = $state.current.data;
      let stateTitle = {
        pageTitle: data.title
      };
      return this._constructTitle(stateTitle.pageTitle);
    };
      
    this.subscribe = function(scope, callback) {
      let handler = $rootScope.$on('title-event', callback);
      scope.$on('$destroy', handler);
    };
    
    this.publish = function(title) {
      $rootScope.$emit('title-event', this._constructTitle(title));
    };
  });