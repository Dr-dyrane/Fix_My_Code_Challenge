#!/usr/bin/ruby
###############################################################################
# Sort Integer Arguments
#
# This script sorts the integer arguments provided in ascending order.
#
# Usage:
#   ./2-sort.rb <integer1> <integer2> ...
#
# Example:
#   ./2-sort.rb 12 41 2 9 -9 31 -1 32
#   Output: -9 -1 2 9 12 31 32 41
#
# Author:
# - Alexander Udeogaranya
###############################################################################

# Collect integer arguments
result = ARGV.select { |arg| arg.match?(/^(-?\d+)$/) }.map(&:to_i)

# Sort the integer arguments in ascending order
result.sort!

# Print the sorted integers
result.each { |num| puts num }
