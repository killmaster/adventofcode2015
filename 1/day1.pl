#!/usr/bin/perl
use strict;
use warnings;

use Path::Class;
use autodie;

my $file = file("day1input.txt");

my $file_contents = $file->slurp();

my $count_up = () = $file_contents =~ m/\(/g;
my $count_down = () = $file_contents =~ m/\)/g;

my $floor = $count_up - $count_down;

my $current = 0;
my $count = 0;
while ($file_contents =~ m/([\(\)])/g) {
  my $char = $1;
  if($char =~ m/\(/) {
    $current++;
  } else {
    $current--;
  }
  $count++;
  if($current < 0) {
    last;
  }
}
print "part 1: $floor\n";
print "part 2: $count\n";
