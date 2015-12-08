#!/usr/bin/perl
use strict;
use warnings;

use Path::Class;
use autodie;

my $file = file("input.txt");

my @file_contents = $file->slurp();

my $count_total = 0;
my $count_sanitized = 0;
my $cound_encoded = 0;
foreach my $line (@file_contents) {
  $count_total += length $line;
  my $sanitized = $line;
  my $encoded = $line;
  $sanitized =~ s/\\\\/\//g;
  $sanitized =~ s/\\x.//g;
  $sanitized =~ s/\\"/(/g;
  $sanitized =~ s/"//g;
  $count_sanitized += length $sanitized;
  $encoded =~ s/\\/\\\\/g;
  $encoded =~ s/"/\\"/g;
  $encoded =~ s/^/"/g;
  $encoded =~ s/\n/"\n/g;
  $cound_encoded += length $encoded;
  print $encoded;
}
print "$count_total\n";
print "$count_sanitized\n";
print "$cound_encoded\n";

print "result part1: ", $count_total-$count_sanitized, "\n";
print "result part2: ", $cound_encoded-$count_total, "\n";
