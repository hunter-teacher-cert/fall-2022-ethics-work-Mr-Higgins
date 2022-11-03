Hopefully this write-up is not intended to be a coded algorithm, but more of a description.

# The Algorithm

The meat and potatoes of this algorithm is actually inspired by [this paper](https://tidel.mie.utoronto.ca/pubs/Theses/vidotto.phd.pdf) which is a thesis attempting to tackle the constraint programming problem of managing tables in restaurants.

The algorithm would of course be adjusted to the following constraints:
* Groups are treated as contiguous entities and any or all splits will be treated as an algorithmic loss of efficiency (this could be quantified by some form of efficiency scoring, or the airline themselves could offer discounts or rewards for groups that opt in for splitting).
* Booking reservations or standby is on a first-come, first-serve basis. Standby is still not a guarantee of passage.
* Customer history of cancellations will not be utilized by the algorithm, cancellation policies and penalties will be left to airline design. (There is always room for algorithm abuse, this is admittedly the constraint I spent the most time thinking upon, but for the sake of completeness I left it in this state.)
* Customer choices (seating preference such as aisle or window, aft or forward, etc.) will only be available for flights booked ahead, likely a dynamic window dependent on business.
* The aisle will be considered a form of splitting, but of course changes in row will be a higher value/penalty of splitting.
* Groups larger than a contiguous row will only incur splitting penalties if any member is not adjacent to another.
* Specific seating requests (numbered seating) is not an option.
* Until the seating chart is finalized, a portion of the cabin should be considered highest-penalty to allow for at minimum average expectancy for the elderly or mobility-accommodated.
* During the booking window, if a group elect preferences that are available on an earlier flight with the same qualifications (location of departure and arrival) the system _must_ allow for user choice.
* In addition to the above, seating qualities (contiguous group seating, seating preferences) *must be a guarantee* once booking has occurred. There may be some extraneous system in place to offer bonuses/discounts for "trading in" these preferences for rewards (so long as it benefits the efficiency of the system solution) but this would require user acceptance.
* There is no need for seating charts to be finalized until boarding time. Seats left available will be committed to standby customers.
* Solutions **must** adhere to airline requirements for weight balance and distribution. No solution that breaks this will be considered successful.

# Benefits
By removing seating choice (and allowing preference of seating type) we now have a dynamic system that can accommodate many forms of cancellation and group size. By placing honesty and transparency in the reservations/booking system, customers know that their preferences *will be guaranteed* once the booking is complete. In addition, instead of adding a price penalty for groups attempting to stay together, pricing instead becomes *discount/reward* focused for customers willing to trust in the system or only list fewer preferences. In particular, I feel showing the earliest flight (or set of flights in their time range) that *accommodates* a group preference in addition to an earliest flight (or set of flights in their time range) that lacks one or more of these preferences gives customers insight to help make their decision.

# Implementation Issues
One quick issue will be most visible during peak booking periods. Simultaneous reservations with groups may result in many "bounce back" moments that could frustrate customers because another group of customers got there first. This should occur _less_ often since seat preferences are no longer a default, but it still will be a large hurdle for the system to overcome.

The greatest issue I forsee is actually _group resizing_. Suppose a group isn't *cancelling* but *resizes*. Upsizing isn't the challenge here, if anything upsizing should be easier to accommodate in those rare cases, no instead *downsizing* is troublesome because it can be *exploitative* as it's not necessarily a *cancellation*. An airline would need an airtight policy to mitigate these situations, or at the very least, will need to ensure a craft with a high quantity of standby passengers can still meet the economic needs of the company.

One issue, that isn't necessarily coding-related, is customer trust. You can show all the data in the world, but there will still be a level of "is this really the situation or am I being bamboozled?" And in all honesty, the best way to work around this is to ***not ever rely on customer history or browser cookies to manipulate pricing***. The only time customer history should ever play into pricing is if the customer has some exploitative behavior, which would go into company policy rather than an algorithmic result.