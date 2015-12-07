#!/usr/bin/perl
use strict;
use warnings;

use Path::Class;
use autodie;

my $file = file("day2input.txt");

my @file_contents = $file->slurp();

my $total = 0;
my $ribbon = 0;
foreach my $box (@file_contents) {
  chomp $box;
  my @dims = split(/x/, $box);
  @dims = sort {$a <=> $b} @dims;
  $total += (2 * $dims[0] * $dims[1]) + (2 * $dims[0] * $dims[2]) + (2 * $dims[1] * $dims[2]) + ($dims[0] * $dims[1]);
  $ribbon += (2 * $dims[0] + 2 * $dims[1]) + ($dims[0] * $dims[1] * $dims[2]);
}

print "part 1: $total\n";
print "part 2: $ribbon\n";
