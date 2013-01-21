'use strict';

var FetcherCtrl = ['$scope', 'ParseService', function($scope, ParseService){
  $scope.users = {};

  ParseService.getAllCheckouts().then(function(results){
    angular.forEach(results, function(val){
      var attribs = val.attributes;
      if (!$scope.users[attribs.user_email]) $scope.users[attribs.user_email] = [];
      // users[email] is an array of checkouts
      $scope.users[attribs.user_email].push(val);
    });
  }, function(error){
    alert(error.message);
  });

  ParseService.getAllPushes().then(function(results){
    $scope.pushes = results;
  }, function(error){
    alert(error.message);
  });
}];
