#!/usr/bin/perl
use strict;
use warnings;

use Path::Class;
use autodie;

my $file = file("day6input.txt");

my @file_contents = $file->slurp();

my $lights = {};
my $lights_part2 = {}; 

my $count = 0;
my $brightness = 0;

foreach my $line (@file_contents) {
  chomp $line;
  $line =~ /^(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)/;
  my $instruction = $1;
  my ($x1,$y1) = ($2,$3);
  my ($x2,$y2) = ($4,$5);
  my $x = $x1;
  while ($x <= $x2) {
    my $y = $y1;
    while ($y <= $y2) {
      $y++;
      $lights_part2->{$x}{$y} = 0 unless defined $lights_part2->{$x}{$y};
      if ($instruction =~ m/on/) {
        $lights->{$x}{$y} = 1;
        $lights_part2->{$x}{$y} += 1;
      } if ($instruction =~ m/off/) {
          $lights->{$x}{$y} = 0;
          next if $lights_part2->{$x}{$y} == 0;
          $lights_part2->{$x}{$y} -= 1; 
      } if ($instruction =~ m/toggle/) {
          $lights->{$x}{$y} = 0 unless defined $lights->{$x}{$y};
          $lights->{$x}{$y} = 1 - $lights->{$x}{$y};
          $lights_part2->{$x}{$y} += 2;
      }
    }
    $x++;
  }
}


foreach my $x (keys %$lights) {
  foreach my $y (keys %{$lights->{$x}}) {
    if ($lights->{$x}{$y}) {
      $count++;
    }
  }
}

print "part 1: $count\n";

foreach my $x (keys %$lights_part2) {
  foreach my $y (keys %{$lights_part2->{$x}}) {
    if ($lights_part2->{$x}{$y}) {
      $brightness += $lights_part2->{$x}{$y};
    }
  }
}


print "part 2: $brightness\n";
