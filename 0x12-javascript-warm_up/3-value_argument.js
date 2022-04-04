#!/usr/bin/node

if (_.isEmpty(argv.$1)) {
  console.log('No argument');
} else {
  console.log(argv.$1);
}
