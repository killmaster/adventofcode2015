#!/usr/bin/perl
use strict;
use warnings;

use Path::Class;
use autodie;

my $file = file("day3input.txt");

my $file_contents = $file->slurp();
chomp($file_contents);

my @characters = split //, $file_contents;

my $x = 0;
my $y = 0;
my $w = 0;
my $z = 0;

my $iterator = 0;

my $world = {};

$world->{$x}{$y} = 1;
foreach my $character (@characters) {
  if ($character eq '>') {
    $iterator % 2 == 0 ? $x++ : $w++;
  } elsif ($character eq '<') {
    $iterator % 2 == 0 ? $x-- : $w--;
  } elsif ($character eq '^') {
    $iterator % 2 == 0 ? $y++ : $z++;
  } elsif ($character eq 'v') {
    $iterator % 2 == 0 ? $y-- : $z--;
  }
  $iterator % 2 == 0 ? $world->{$x}{$y} += 1 : $world->{$w}{$z} += 1;
  $iterator++;
}

my $count = 0;
foreach my $i (keys %$world) {
  foreach my $j (keys %{$world->{$i}}) {
    $count++;
  }
}
#print "part 1: $count\n";
print "part 2: $count\n";
