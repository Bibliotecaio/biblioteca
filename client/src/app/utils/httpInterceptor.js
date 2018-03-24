angular.module('httpInterceptor', [
  'toaster'
])

.factory('httpInterceptor',
  function httpInterceptor($q, $injector) {
    return {
      request: function (config) {
        return config;
      },
      
      responseError: function (response) {
        
        let Toaster = $injector.get('toaster');
        
        if(response.status <= 0) {
          Toaster.error({
            body: 'Сервер недоступен'
          });
          return $q.reject(response);
        } else if (response.status === 404) {
           $injector.get('$state').transitionTo('admin.documents.all');
           Toaster.error({
             title: 'Страница не найдена',
             body: 'Ошибка 404'
            });
            return $q.reject(response);
        } else if (response.status === 500) {
          Toaster.error({
            title: response.status,
            body: 'Ошибка сервера'
          });
        }
      }
   };
});