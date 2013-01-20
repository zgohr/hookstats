'use strict';

angular.module('DataServices', [])
  .factory('ParseService', ['$q', '$timeout', function($q, $timeout){
    Parse.initialize("ElAH6C9vFmBLeO09O5qD0PgUfX0bA6v2zqiGap1L",
                     "Lk6FuM21JfvXbeNX11YZNrd1cJHelnv6pMOP85Z4");

    var Checkout = Parse.Object.extend('Checkout');
    var Push = Parse.Object.extend('Push');

    return {
      getAllCheckouts: function() {
        var deferred = $q.defer();
        var query = new Parse.Query(Checkout);
        query.descending('createdAt');
        query.find({
          success: function(results){
            $timeout(function(){
              deferred.resolve(results);
            })
          },
          error: function(error){
            $timeout(function(){
              deferred.reject(error);
            });
          }
        });
        return deferred.promise;
      },
      getAllPushes: function() {
        var deferred = $q.defer();
        var query = new Parse.Query(Push);
        query.descending('createdAt');
        query.find({
          success: function(results){
            $timeout(function(){
              deferred.resolve(results);
            });
          },
          error: function(error){
            $timeout(function(){
              deferred.reject(error);
            });
          }
        });
        return deferred.promise;
      }
    };
  }]);
