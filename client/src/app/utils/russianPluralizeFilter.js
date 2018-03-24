angular.module('russianPluralizeFilter', [
])

.filter('russian_pluralize', function russianPluralizeFilter() {
      /**
       * Функция getPlural возвращает окончание для множественного числа слова
       * на основании числа и массива окончаний
       * @param  number Integer Число на основе которого нужно сформировать
       * окончание
       * @param  endingsArr Array Массив слов или окончаний
       *         для чисел (1, 4, 5),
       *         например ['яблоко', 'яблока', 'яблок']
       * @return String
       */

      function getPlural(number, endingsArr) {
        number = Math.abs(number);
        number %= 100;

        if (number >= 5 && number <= 20) {
          return endingsArr[2];
        }

        number %= 10;
        if (number === 1) {
          return endingsArr[0];
        }

        if (number >= 2 && number <= 4) {
          return endingsArr[1];
        }

        return endingsArr[2];
      }

      return function(input, arr){
        return getPlural(input, arr);
      };
    });


