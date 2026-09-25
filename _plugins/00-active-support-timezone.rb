# frozen_string_literal: true

# Jekyll plugins use ActiveSupport for date formatting. Choose the Rails 8.1
# timezone behavior before the first conversion so builds remain warning-free.
require "active_support"

ActiveSupport.to_time_preserves_timezone = :zone
