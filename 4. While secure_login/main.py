count = 0
stop = False

while count < 5 or stop == False:
    print(count)
    count += 1
    if count == 3:
        stop = True
        


শুরুতে মানগুলো (Initialization):
count এর মান হলো 0

stop এর মান হলো False

প্রথমবার লুপ ঘোরা (Iteration 1):
while লুপের শর্ত চেক করা হলো: count < 5 or stop == False

এখানে count < 5 হলো 0 < 5 (সত্য বা True)।

মাঝখানে আছে or (অর্থাৎ যেকোনো একটি সত্য হলেই লুপ চলবে)।

তাই পুরো শর্তটি সত্য হলো এবং লুপের ভেতরে প্রবেশ করল।

print(count) এর মাধ্যমে স্ক্রিনে প্রিন্ট হলো: 0

count += 1 হওয়ার কারণে count এর মান বেড়ে হলো 1

if count == 3: চেক করা হলো। 1 এবং 3 সমান নয়, তাই এই শর্ত মিলল না।



দ্বিতীয়বার লুপ ঘোরা (Iteration 2):

while লুপের শর্ত চেক করা হলো: count < 5 or stop == False

count এর মান এখন 1, যা 5 এর চেয়ে ছোট (সত্য)।

তাই লুপ আবার ঘুরবে।

print(count) এর মাধ্যমে স্ক্রিনে প্রিন্ট হলো: 1

count += 1 হওয়ার কারণে count এর মান বেড়ে হলো 2

if count == 3: চেক করা হলো। 2 এবং 3 সমান নয়, তাই শর্ত মিলল না।



তৃতীয়বার লুপ ঘোরা (Iteration 3):
while লুপের শর্ত চেক করা হলো: count < 5 or stop == False

count এর মান এখন 2, যা 5 এর চেয়ে ছোট (সত্য)।

তাই লুপ আবার ঘুরবে।

print(count) এর মাধ্যমে স্ক্রিনে প্রিন্ট হলো: 2

count += 1 হওয়ার কারণে count এর মান বেড়ে হলো 3

if count == 3: চেক করা হলো। এবার 3 এবং 3 মিলে গেল!

ফলে stop = True হয়ে গেল। (অর্থাৎ stop এর মান এখন থেকে সত্যি হলো)।



চতুর্থবার লুপ ঘোরা (Iteration 4):

while লুপের শর্ত চেক করা হলো: count < 5 or stop == False

এখানে count < 5 হলো 3 < 5 (যা এখনো সত্য)।

কিন্তু stop == False অংশটি এখন মিথ্যা হয়ে গেছে, কারণ stop এর মান ইতিমধ্যে True হয়ে গেছে (True == False মানে মিথ্যা)।

যেহেতু মাঝখানে or আছে এবং প্রথম অংশটি (3 < 5) সত্য, তাই পুরো শর্তটি এখনো সত্য বলে গণ্য হবে! ফলে লুপ বন্ধ না হয়ে আবারও ঘুরবে।

print(count) এর মাধ্যমে স্ক্রিনে প্রিন্ট হলো: 3

count += 1 হওয়ার কারণে count এর মান বেড়ে হলো 4

ভেতরের if count == 3: শর্তটি আর মিলল না।



পঞ্চমবার লুপ ঘোরা (Iteration 5):

while লুপের শর্ত চেক করা হলো: count < 5 or stop == False

count এর মান এখন 4, যা 5 এর চেয়ে ছোট (সত্য)।

তাই লুপ আবারও ঘুরবে।

print(count) এর মাধ্যমে স্ক্রিনে প্রিন্ট হলো: 4

count += 1 হওয়ার কারণে count এর মান বেড়ে হলো 5

ভেতরের if শর্ত মিলল না।



ষষ্ঠবার লুপ চেক (Loop Termination):
while লুপের শর্ত চেক করা হলো: count < 5 or stop == False

count < 5 মানে 5 < 5 (এবার এটি মিথ্যা বা False)।

stop == False মানে True == False (এটিও মিথ্যা বা False)।

যেহেতু or-এর দুই পাশের অংশই মিথ্যা হয়ে গেছে, তাই পুরো while শর্তটি মিথ্যা হয়ে গেল।

ফলস্বরূপ, লুপটি এখানেই চিরতরে বন্ধ বা টার্মিনেট হয়ে গেল।

চূড়ান্ত আউটপুট:

কোডটি রান করার পর কনসোলে যে সংখ্যাগুলো প্রিন্ট হবে:

Plaintext
0
1
2
3
4
এখানে লক্ষ্য করার বিষয় হলো, stop = True করার পরেও লুপটি থেমে যায়নি, 

কারণ or এর কারণে count < 5 শর্তটি তখনও সত্য ছিল! প্রোগ্রামিং লজিক শেখার জন্য এই খুঁটিনাটি বিষয়গুলো বোঝা খুবই জরুরি।





count = 0
start = False

# লুপটি চলবে যতক্ষণ count ৫ এর কম অথবা start == False থাকে
while count < 5 or start == False:
    print(f"Current count: {count}, Start: {start}")
    
    # যদি start সত্য হয়, তবে count বাড়াতে থাকব
    if start:
        count += 1
    # না হলে প্রথমে start কে True করে দেবো
    else:
        start = True


শুরুতে মানগুলো (Initialization):

count এর মান শুরু হলো 0 দিয়ে।

start এর মান শুরু হলো False দিয়ে।



প্রথমবার লুপ ঘোরা (Iteration 1):
while লুপের শর্ত চেক করা হলো: count < 5 or start == False

এখানে count < 5 মানে 0 < 5 (সত্য বা True)।

মাঝখানে or থাকার কারণে পুরো শর্তটি সত্য হলো এবং লুপের ভেতরে প্রবেশ করল।

প্রিন্ট হলো: Current count: 0, Start: False

ভেতরের if start: চেক করা হলো। যেহেতু start এর মান False, তাই এটি if ব্লক বাদ দিয়ে else ব্লকে চলে গেল।

else ব্লকের কাজ: start = True (অর্থাৎ start এর মান পরিবর্তন হয়ে এখন থেকে True হয়ে গেল)।



দ্বিতীয়বার লুপ ঘোরা (Iteration 2):
while লুপের শর্ত চেক করা হলো: count < 5 or start == False

count < 5 মানে 0 < 5 (সত্য)।

start == False মানে True == False (মিথ্যা)।

যেহেতু মাঝখানে or আছে এবং প্রথম অংশটি সত্য, তাই পুরো শর্তটি সত্য হলো এবং লুপ আবার ঘুরল।

প্রিন্ট হলো: Current count: 0, Start: True

ভেতরের if start: চেক করা হলো। এবার start এর মান True হওয়ায় কোড সরাসরি if ব্লকের ভেতরে প্রবেশ করল।

if ব্লকের কাজ: count += 1 (আগের 0 এর সাথে 1 যোগ হয়ে count এর মান এখন হলো 1)।



তৃতীয়বার লুপ ঘোরা (Iteration 3):
while লুপের শর্ত চেক করা হলো: count < 5 or start == False

count < 5 মানে 1 < 5 (সত্য)।

তাই লুপ আবারও ঘুরল।

প্রিন্ট হলো: Current count: 1, Start: True

if start: সত্য হওয়ায় count += 1 হলো (আগের 1 এর সাথে 1 যোগ হয়ে count হলো 2)।



চতুর্থবার লুপ ঘোরা (Iteration 4):
count এর মান 2, যা 5 এর চেয়ে ছোট (সত্য)। লুপ ঘুরল।

প্রিন্ট হলো: Current count: 2, Start: True

count += 1 হওয়ার কারণে count এর মান বেড়ে হলো 3।



পঞ্চমবার লুপ ঘোরা (Iteration 5):
count এর মান 3, যা 5 এর চেয়ে ছোট (সত্য)। লুপ ঘুরল।

প্রিন্ট হলো: Current count: 3, Start: True

count += 1 হওয়ার কারণে count এর মান বেড়ে হলো 4।



ষষ্ঠবার লুপ ঘোরা (Iteration 6):
count এর মান 4, যা 5 এর চেয়ে ছোট (সত্য)। লুপ ঘুরল।

প্রিন্ট হলো: Current count: 4, Start: True

count += 1 হওয়ার কারণে count এর মান বেড়ে হলো 5।



সপ্তমবার লুপ ঘোরা (Iteration 7):
count এর মান 5, যা 5 এর চেয়ে ছোট নয় (মিথ্যা)।

start == False মানে True == False (এটিও মিথ্যা)।

or এর দুই পাশের অংশই মিথ্যা হওয়ায় while লুপের শর্ত আর মিলল না। ফলে লুপটি এখানেই চিরতরে বন্ধ বা টার্মিনেট হয়ে গেল।

চূড়ান্ত আউটপুট:
কোডটি রান করার পর কনসোলে যে লেখাগুলো প্রিন্ট হবে:

Plaintext
Current count: 0, Start: False
Current count: 0, Start: True
Current count: 1, Start: True
Current count: 2, Start: True
Current count: 3, Start: True
Current count: 4, Start: True
এখানে একটা মজার বিষয় খেয়াল করুন: প্রথমবার লুপ চলার সময় count না বাড়িয়ে শুধু start কে True করা হয়েছে,
যে কারণে 0 সংখ্যাটি দুইবার প্রিন্ট হয়েছে (একবার Start: False নিয়ে এবং একবার Start: True নিয়ে)। লজিক বিল্ডিংয়ের জন্য এটি দারুণ একটি ট্রিক!




এপিআই রেট লিমিটিং লজিক (API Rate Limiting / Traffic Control)
ব্যাকএন্ড সার্ভারকে স্প্যাম বা অতিরিক্ত ট্রাফিকের হাত থেকে রক্ষা করার জন্য রেট লিমিটিং ব্যবহার করা হয়।
কোনো ইউজার নির্দিষ্ট লিমিটের চেয়ে বেশি রিকোয়েস্ট পাঠালে তাকে ব্লক বা হোল্ড করে রাখা হয়:

request_count = 0
max_limit = 3

# ইনকামিং রিকোয়েস্টগুলোর একটি লিস্ট
incoming_requests = ["req_1", "req_2", "req_3", "req_4", "req_5"]

for req in incoming_requests:
    request_count += 1
    
    # রিকোয়েস্ট লিমিট পার হয়ে গেছে কি না তা চেক করা হচ্ছে
    if request_count > max_limit:
        print(f"Blocked: Too many requests. {req} is rejected.")
    else:
        print(f"Allowed: Processing {req}.")


শুরুতে মানগুলো (Initialization):
request_count এর মান হলো 0

max_limit এর মান হলো 3 (অর্থাৎ সর্বোচ্চ ৩টি রিকোয়েস্ট পাস হতে পারবে)

incoming_requests লিস্টে মোট ৫টি রিকোয়েস্ট আছে: ["req_1", "req_2", "req_3", "req_4", "req_5"]



প্রথমবার লুপ ঘোরা (Iteration 1):
req ভেরিয়েবলের ভেতরে আসল প্রথম রিকোয়েস্ট: "req_1"

request_count += 1 হওয়ার কারণে request_count এর মান বেড়ে হলো 1

শর্ত চেক করা হলো: if request_count > max_limit: অর্থাৎ 1 > 3 (১ কি ৩ এর চেয়ে বড়?)। না, এটি মিথ্যা বা False।

ফলে কোড চলে গেল else ব্লকে।

প্রিন্ট হলো: Allowed: Processing req_1.



দ্বিতীয়বার লুপ ঘোরা (Iteration 2):
req ভেরিয়েবলের ভেতরে আসল দ্বিতীয় রিকোয়েস্ট: "req_2"

request_count += 1 হওয়ার কারণে request_count এর মান বেড়ে হলো 2

শর্ত চেক করা হলো: 2 > 3 (মিথ্যা)।

কোড else ব্লকে প্রবেশ করল।

প্রিন্ট হলো: Allowed: Processing req_2.


    
তৃতীয়বার লুপ ঘোরা (Iteration 3):
req ভেরিয়েবলের ভেতরে আসল তৃতীয় রিকোয়েস্ট: "req_3"

request_count += 1 হওয়ার কারণে request_count এর মান বেড়ে হলো 3

শর্ত চেক করা হলো: 3 > 3 (৩ কি ৩ এর চেয়ে বড়? না, সমান)। এটিও মিথ্যা বা False।

কোড else ব্লকে প্রবেশ করল।

প্রিন্ট হলো: Allowed: Processing req_3.



চতুর্থবার লুপ ঘোরা (Iteration 4):
req ভেরিয়েবলের ভেতরে আসল চতুর্থ রিকোয়েস্ট: "req_4"

request_count += 1 হওয়ার কারণে request_count এর মান বেড়ে হলো 4

শর্ত চেক করা হলো: if request_count > max_limit: অর্থাৎ 4 > 3 (৪ কি ৩ এর চেয়ে বড়?)। হ্যাঁ, এটি সত্য বা True!

শর্ত মিলে যাওয়ার কারণে এবার কোড if ব্লকের ভেতরে প্রবেশ করল।

প্রিন্ট হলো: Blocked: Too many requests. req_4 is rejected.



পঞ্চমবার লুপ ঘোরা (Iteration 5):
req ভেরিয়েবলের ভেতরে আসল পঞ্চম রিকোয়েস্ট: "req_5"

request_count += 1 হওয়ার কারণে request_count এর মান বেড়ে হলো 5

শর্ত চেক করা হলো: 5 > 3 (সত্য)।

কোড আবার if ব্লকের ভেতরে প্রবেশ করল।

প্রিন্ট হলো: Blocked: Too many requests. req_5 is rejected.

লিস্টের সব আইটেম বা রিকোয়েস্ট প্রসেস করা শেষ হওয়ায় লুপটি নিজে থেকেই বন্ধ হয়ে গেল।

চূড়ান্ত আউটপুট:

সম্পূর্ণ কোডটি রান করার পর কনসোলে যে লেখাগুলো দেখা যাবে:

Plaintext
Allowed: Processing req_1.
Allowed: Processing req_2.
Allowed: Processing req_3.
Blocked: Too many requests. req_4 is rejected.
Blocked: Too many requests. req_5 is rejected.







correct_pin = "1234"
attempts_left = 3   # সর্বোচ্চ ৩ বার চেষ্টা করার সুযোগ আছে

print("--- Welcome to ATM System ---")

# While লুপ: ইউজারের যতক্ষণ সুযোগ বাকি থাকবে, লুপটি চলতেই থাকবে
while attempts_left > 0:
    entered_pin = input("Enter your 4-digit PIN code: ")
    
    # If কন্ডিশন ১: পিন সঠিক কি না তা চেক করা
    if entered_pin == correct_pin:
        print("Success! Your account has been unlocked. ✅")
        break  # পিন সঠিক হলে লুপটি সাথে সাথে ভেঙে বের হয়ে যাবে
        
    # Else কন্ডিশন: পিন ভুল হলে এটি রান করবে
    else:
        attempts_left -= 1  # এক দফা সুযোগ কমে গেল
        print(f"Incorrect PIN! ❌ You have {attempts_left} attempt(s) left.")

# ইউজার সব সুযোগ হারিয়ে ফেললে এটি ব্লক করে দেবে
if attempts_left == 0:
    print("Security Alert! 🚨 Your card has been blocked.")


ইনিশিয়ালাইজেশন (Initialization)
correct_pin = "1234"

মেমরিতে correct_pin ভেরিয়েবলের মধ্যে "1234" স্ট্রিংটি সংরক্ষিত হলো।

attempts_left = 3

মেমরিতে attempts_left ভেরিয়েবলে ইন্টিজার মান 3 সেট করা হলো।

print("--- Welcome to ATM System ---")

টার্মিনাল আউটপুটে প্রিন্ট হলো: --- Welcome to ATM System ---

ধাপ ২: প্রথমবার লুপ এক্সিকিউশন (ইউজার ভুল পিন দিল: "0000")
while attempts_left > 0:

শর্ত চেক করা হলো যে 3 > 0 কি না, যা সত্য হিসেবে গণ্য হলো। ফলে এক্সিকিউশন লুপের ভেতরে প্রবেশ করল।

entered_pin = input("Enter your 4-digit PIN code: ")

প্রোগ্রাম ইউজারের ইনপুটের জন্য অপেক্ষা করল। ইউজার দিল "0000"।

if entered_pin == correct_pin:

চেক করা হলো "0000" এবং "1234" সমান কি না, যা মিথ্যা হিসেবে গণ্য হলো। প্রোগ্রাম if ব্লক এড়িয়ে else ব্লকে চলে গেল।

attempts_left -= 1

else ব্লক রান করল। attempts_left-এর মান ১ কমে নতুন মান হলো 2।

print(f"Incorrect PIN! ❌ You have {attempts_left} attempt(s) left.")

টার্মিনাল আউটপুটে প্রিন্ট হলো: Incorrect PIN! ❌ You have 2 attempt(s) left.

ধাপ ৩: দ্বিতীয়বার লুপ এক্সিকিউশন (ইউজার ভুল পিন দিল: "1111")
while attempts_left > 0:

শর্ত চেক করা হলো যে 2 > 0 কি না, যা সত্য। লুপ আবার চলল।

entered_pin = input(...)

ইউজার দিল "1111"।

if entered_pin == correct_pin:

চেক করা হলো "1111" এবং "1234" সমান কি না, যা মিথ্যা।

attempts_left -= 1

attempts_left-এর মান ১ কমে নতুন মান হলো 1।

print(...)

টার্মিনাল আউটপুটে প্রিন্ট হলো: Incorrect PIN! ❌ You have 1 attempt(s) left.

ধাপ ৪: তৃতীয়বার লুপ এক্সিকিউশন (ইউজার সঠিক পিন দিল: "1234")
while attempts_left > 0:

শর্ত চেক করা হলো যে 1 > 0 কি না, যা সত্য। লুপ শেষবারের মতো চলল।

entered_pin = input(...)

ইউজার সঠিক পিন "1234" দিল।

if entered_pin == correct_pin:

চেক করা হলো "1234" এবং "1234" সমান কি না, যা সত্য হিসেবে গণ্য হলো। এক্সিকিউশন if ব্লকের ভেতরে প্রবেশ করল।

print("Success! Your account has been unlocked. ✅")

টার্মিনাল আউটপুটে প্রিন্ট হলো: Success! Your account has been unlocked. ✅

break

ব্রেক কমান্ড রান করল, যা সাথে সাথে while লুপটিকে চিরতরে থামিয়ে দিল এবং এক্সিকিউশনকে লুপের বাইরে নিয়ে গেল।

ধাপ ৫: লুপের বাইরের শেষ মূল্যায়ন
if attempts_left == 0:

চেক করা হলো 1 এবং 0 সমান কি না, যা মিথ্যা হিসেবে গণ্য হলো (কারণ attempts_left-এর মান তখনো 1 ছিল)।

প্রোগ্রাম সমাপ্তি (Program Termination):

শর্ত মিথ্যা হওয়ায় কার্ড ব্লক হওয়ার ওয়ার্নিং মেসেজটি স্কিপ করা হলো এবং প্রোগ্রাম সফলভাবে শেষ হলো।
