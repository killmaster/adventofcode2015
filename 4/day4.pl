#!/usr/bin/perl
use strict;
use warnings;

use Path::Class;
use autodie;
use Digest::MD5 qw(md5_hex);

my $key = 'yzbqklnj';
my $sufix = 0;
my $digest = 'bananas';

while ($digest !~ m/^00000/) {
  $sufix++;
  $digest = md5_hex($key.$sufix);
}

print "part 1: $sufix\n";

while ($digest !~ m/^000000/) {
  $sufix++;
  $digest = md5_hex($key.$sufix);
}

print "part 2: $sufix\n";
