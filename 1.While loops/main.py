count = 0

start = False

while count < 10:
    if start:
      count += 1
      print(count)
    else:
      start = True

১. count = 0

কী হচ্ছে: মেমোরিতে count নামের একটি ভেরিয়েবল তৈরি হলো এবং এতে 0 মান রাখা হলো।

২. start = False

কী হচ্ছে: মেমোরিতে start নামের আরেকটি ভেরিয়েবল তৈরি হলো এবং এর মান রাখা হলো False (অসত্য)।

৩. while count < 10: (লুপের প্রথম ইটারেশন - Loop 1)

কী হচ্ছে: পাইথন চেক করছে count < 10 কি না। যেহেতু count-এর মান 0 এবং 0 < 10 সত্য, তাই লুপের ভেতরে প্রবেশ করল।

৪. if start:

কী হচ্ছে: চেক করা হচ্ছে start সত্য (True) কি না। যেহেতু start-এর মান 0-তে বা আগের লাইনে False সেট করা আছে, তাই শর্তটি মিথ্যা হলো। ফলে if-এর ভেতরের ব্লকটি স্কিপ করে সরাসরি else-এ চলে গেল।

৫. else:

কী হচ্ছে: যেহেতু if মিথ্যা হয়েছে, তাই else-এর ভেلতরের কোড এক্সিকিউট হবে।

৬. start = True

কী হচ্ছে: start ভেরিয়েবলের মান পরিবর্তন হয়ে False থেকে এখন True হয়ে গেল। (প্রথম লুপ শেষ)।

লুপ ২ (Second Iteration):

while count < 10: count-এর মান এখনও 0 আছে, তাই 0 < 10 সত্য। লুপ আবার ভেতরে প্রবেশ করল।

if start: এখন চেক করা হচ্ছে start সত্য কি না। যেহেতু একটু আগে start = True করা হয়েছে, তাই এবার এই শর্তটি সত্য হলো!

count += 1 count-এর বর্তমান মান 0-এর সাথে 1 যোগ হলো। এখন count-νর নতুন মান হলো 1 (0 + 1 = 1)।

print(count) স্ক্রিন বা কনসোলে প্রিন্ট হবে: 1

(else ব্লকটি এইবার আর রান হবে না, কারণ if সত্য হয়ে গেছে)।

লুপ ৩ (Third Iteration):

while count < 10: count-এর মান 1 (1 < 10 সত্য)। লুপ ভেতরে প্রবেশ করল।

if start: start এখনও True, তাই শর্ত সত্য।

count += 1 count-এর মান ১ বেড়ে হলো 2 (1 + 1 = 2)।

print(count) কনসোলে প্রিন্ট হবে: 2

(এভাবে লুপটি চলতে থাকবে। প্রতিবার count-এর মান ১ করে বাড়বে এবং else ব্লকটি আর কখনো কাজ করবে না কারণ start চিরতরে True হয়ে গেছে।)

লুপ ১১ (শেষের আগের ইটারেশন - যখন count = 9):

while count < 10: count-এর মান 9 (9 < 10 সত্য)। লুপ ভেতরে প্রবেশ করল।

if start: শর্ত সত্য।

count += 1 count-এর মান ১ বেড়ে হলো 10 (9 + 1 = 10)।

print(count) কনসোলে প্রিন্ট হবে: 10

লুপ ১২ (Termination / লুপ শেষ হওয়া):

while count < 10: পাইথন চেক করে দেখল count-এর মান এখন 10, আর 10 < 10 শর্তটি মিথ্যা (False)।

ফলে while লুপের চেইন ভেঙে বা টার্মিনেট হয়ে প্রোগ্রাম এখানেই শেষ হয়ে গেল।

চূড়ান্ত আউটপুট (Final Output):


1
2
3
4
5
6
7
8
9
10




# count = 0

# start = False

# while count < 5 or not start:
#     user_input = input("Enter 'start' to begin or 'exit' to quit: ").strip().lower()
    
#     if user_input == 'start':
#       start = True
      
      
#       print("Starting the process...")
#     elif user_input == 'exit':
#       print("Exiting the program.")
#       break
#     else:
#       print("Invalid input. Please try again.")
    
#     count += 1
  


উদাহরণ ১: ডাইনামিক লিস্ট ম্যানেজার (যতক্ষণ ইচ্ছা ডেটা যোগ করা)
এই কোডটি বারবার ইউজারের কাছ থেকে নাম্বার নেবে। নাম্বারটি লিস্টে আগে থেকেই থাকলে বলবে আছে,
আর না থাকলে লিস্টে যোগ করে নতুন লিস্ট দেখাবে। ইউজার নিজে quit না লেখা পর্যন্ত লুপটি চলতেই থাকবে।

nums = [10, 20, 30]

print("--- Number Management System Started ---")

while True:
    user_input = input("Enter a number (type 'quit' to exit): ")
    
    if user_input.lower() == 'quit':
        print("Program ended! Final list:", nums)
        break
        
    n = int(user_input)
    
    if n in nums:
        print(f"⚠️ {n} is already in the list!\n")
    else:
        nums.append(n)
        print(f"✅ {n} added successfully!")
        print("Updated list:", nums, "\n")





উদাহরণ ২: সিকিউরিটি পিন বা লগইন সিস্টেম (ভুল করলে বারবার সুযোগ দেওয়া)
ব্যাকএন্ডে ইউজারের পাসওয়ার্ড বা পিন ভেরিফিকেশন করার সময় এই লজিকটি সবচেয়ে বেশি ব্যবহার করা হয়। 
ইউজার সঠিক পিন না দেওয়া পর্যন্ত লুপ ঘুরতে থাকে।


pin = "1234"
tries = 3

while tries > 0:
    entered = input("Enter your 4-digit PIN: ")
    
    if entered == pin:
        print("🎉 Login successful! Welcome.")
        break  # সঠিক হলে লুপ শেষ
    else:
        tries -= 1
        print(f"❌ Wrong PIN! You have {tries} attempts left.\n")

# ৩ বার ভুল হলে
if tries == 0:
    print("🚨 Account temporarily blocked!")









CSV ফাইল বা লোগ ফাইল পড়ার সময় 'হেডার' (Header) স্কিপ করা
ব্যাকএন্ড ডেভলপমেন্টে প্রায়ই ব্যবহারকারীর আপলোড করা CSV ফাইল বা সিস্টেমের লগ ফাইল প্রসেস করতে হয়।
সিএসভি ফাইলের প্রথম লাইনটি সাধারণত কলামের নাম বা হেডার থাকে (যেমন: Name, Email, Age)।
প্রথম লাইনটি ডেটা হিসেবে প্রসেস না করে স্কিপ করার জন্য ঠিক এই ধরনের ফ্ল্যাগ লজিক ব্যবহার করা হয়:


is_header_skipped = False
row_count = 0

# ধরে নিই এটি ফাইলের লাইনগুলোর লুপ
file_lines = ["header_name_email", "user1@gmail.com", "user2@gmail.com"]

for line in file_lines:
    if not is_header_skipped:
        # প্রথম লাইনে আসলে ফ্ল্যাগ ট্রু করে দিয়ে লাইনটি স্কিপ করা হচ্ছে
        is_header_skipped = True
        print("-> Header line skipped.")
        continue
    
    # আসল ডেটা প্রসেসিং শুরু
    row_count += 1
    print(f"Processing: {line}")


শুরুতে (Initialization):

is_header_skipped এর মান নির্ধারণ করা হলো False

row_count এর মান নির্ধারণ করা হলো 0

file_lines লিস্টে মোট তিনটি আইটেম আছে: "header_name_email", "user1@gmail.com", এবং "user2@gmail.com"

প্রথমবার লুপ ঘোরা (Iteration 1):

line ভেরিয়েবলের মধ্যে প্রথম মান আসল: "header_name_email"

শর্ত চেক: if not is_header_skipped: (যেহেতু is_header_skipped এর মান False ছিল, তাই not False মানে দাঁড়াল সত্য বা True)। ফলে শর্ত মিলে গেল।

ফ্ল্যাগ পরিবর্তন: is_header_skipped = True (এখান থেকে ফ্ল্যাগের মান পরিবর্তন হয়ে স্থায়ীভাবে True হয়ে গেল)।

প্রিন্ট হলো: Header line skipped.

continue কমান্ড পাওয়ার সাথে সাথে পাইথন এই লুপের নিচের কাজগুলো আর না করে সরাসরি পরের লুপে চলে গেল।

দ্বিতীয়বার লুপ ঘোরা (Iteration 2):

line ভেরিয়েবলের মধ্যে দ্বিতীয় মান আসল: "user1@gmail.com"

শর্ত চেক: if not is_header_skipped: (কিন্তু একটু আগেই তো আমরা ফ্ল্যাগের মান True বানিয়ে দিয়েছি! তাই not True মানে দাঁড়াল মিথ্যা বা False)। ফলে শর্ত আর মিলল না।

পাইথন if ব্লকের ভেতরে আর ঢুকল না, সোজা নিচে নেমে আসল।

row_count += 1 (আগের 0 এর সাথে 1 যোগ হয়ে row_count এখন হলো 1)।

প্রিন্ট হলো: Processing: user1@gmail.com

তৃতীয়বার লুপ ঘোরা (Iteration 3):

line ভেরিয়েবলের মধ্যে তৃতীয় বা শেষ মান আসল: "user2@gmail.com"

শর্ত চেক: is_header_skipped এর মান এখনো True থাকায় শর্ত আবার মিলে নাই।

row_count += 1 (আগের 1 এর সাথে 1 যোগ হয়ে row_count এখন হলো 2)।

প্রিন্ট হলো: Processing: user2@gmail.com

চূড়ান্ত আউটপুট:
লুপ শেষ হওয়ার পর টার্মিনালে বা কনসোলে এই লেখাগুলো দেখা যাবে:

Plaintext
Header line skipped.
Processing: user1@gmail.com
Processing: user2@gmail.com




ডাটাবেজ কানেকশন বা এপিআই রিট্রি (Retry Mechanism)
ব্যাকএন্ড সার্ভার যখন কোনো থার্ড-পার্টি এপিআই (API) বা ডাটাবেজে রিকোয়েস্ট পাঠায়, তখন কানেকশন ফেল করতে পারে। 
প্রথমবার কানেক্ট করার চেষ্টা করার পর যদি ফেইল করে, তখন একটি ফ্ল্যাগ বা স্টেট পরিবর্তন করে সেকেন্ড ট্রাই বা ব্যাকঅফ (Backoff) লজিক চালানো হয়:

connection_attempt = 0
is_connected = False

while connection_attempt < 3:
    if is_connected:
        print("Querying data from database...")
        break
    else:
        print(f"Attempting connection... Attempt no. {connection_attempt + 1}")
        # Let's assume it fails the first time, and connects on the second attempt
        connection_attempt += 1
        if connection_attempt == 2:
            is_connected = True
            print("Connection successful!")



শুরুতে মানগুলো (Initialization):

connection_attempt এর মান শুরু হলো 0 দিয়ে।

is_connected এর মান হলো False (অর্থাৎ শুরুতে কানেক্টেড নয়)।

প্রথমবার লুপ ঘোরা (First Iteration):

while connection_attempt < 3 শর্ত চেক করা হলো। 0 তো 3 এর চেয়ে ছোট, তাই লুপের ভেতরে ঢুকল।

if is_connected: চেক করা হলো। is_connected এর মান False থাকায় if ব্লক বাদ দিয়ে কোড চলে গেল else ব্লকে।

প্রিন্ট হলো: Attempting connection... Attempt no. 1 (যেহেতু connection_attempt ছিল 0, তার সাথে 1 যোগ হয়ে 1 প্রিন্ট হয়েছে)।

connection_attempt += 1 এর কারণে connection_attempt এর মান বেড়ে এখন হলো 1।

ভেতরের if connection_attempt == 2 চেক করা হলো। 1 আর 2 সমান নয়, তাই এই শর্ত মিলল না।

দ্বিতীয়বার লুপ ঘোরা (Second Iteration):

connection_attempt এর বর্তমান মান 1, যা 3 এর চেয়ে ছোট। তাই লুপ আবার ঘুরল।

if is_connected: চেক করা হলো। এটি এখনো False, তাই কোড আবার else ব্লকে প্রবেশ করল।

প্রিন্ট হলো: Attempting connection... Attempt no. 2 (যেহেতু 1 + 1 = 2)।

connection_attempt += 1 এর কারণে connection_attempt এর মান বেড়ে এবার হলো 2।

ভেতরের if connection_attempt == 2 চেক করা হলো। এবার 2 এবং 2 মিলে গেল!

ফলে is_connected = True সেট হয়ে গেল (অর্থাৎ কানেকশন পেয়ে গেছে)।

প্রিন্ট হলো: Connection successful!

তৃতীয়বার লুপ ঘোরা (Third Iteration):

connection_attempt এর বর্তমান মান 2, যা এখনো 3 এর চেয়ে ছোট। তাই লুপ আবারও ঘুরল।

if is_connected: চেক করা হলো। একটু আগেই আমরা is_connected এর মান True করে দিয়েছি!

শর্ত মিলে যাওয়ার কারণে এবার পাইথন if ব্লকের ভেতরে প্রবেশ করল।

প্রিন্ট হলো: Querying data from database...

ঠিক তখনই সামনে পেল break কমান্ড। break পাওয়ার সাথে সাথে পাইথন সম্পূর্ণ লুপটি চিরতরে বন্ধ বা টার্মিনেট করে দিল।

চূড়ান্ত আউটপুট:
পুরো কোড রান করার পর স্ক্রিনে এই লেখাগুলো দেখা যাবে:

Plaintext
Attempting connection... Attempt no. 1
Attempting connection... Attempt no. 2
Connection successful!
Querying data from database...




মেইনটেন্যান্স মোড বা সিস্টেম গেটকিপিং (Feature Flag / Maintenance Switch)
ব্যাকএন্ড সার্ভারে কোনো নতুন ফিচার রান করার আগে বা সিস্টেম মেইনটেন্যান্স মোডে থাকলে রিকোয়েস্ট ব্লক করার জন্য এই ধরনের লজিক ব্যবহার করা হয়:

request_count = 0
is_maintenance_mode = True

while request_count < 5:
    request_count += 1
    
    if is_maintenance_mode:
        print(f"Request #{request_count}: Server is in maintenance mode. Please try again later.")
        
        if request_count == 3:
            is_maintenance_mode = False
            print("--- Server is now live! ---")
    else:
        print(f"Request #{request_count}: Successfully processed.")


শুরুতে মানগুলো (Initialization):

request_count এর মান শুরু হলো 0 দিয়ে।

is_maintenance_mode এর মান হলো True (অর্থাৎ সার্ভার এখন মেইনটেন্যান্স মোডে আছে)।

প্রথমবার লুপ ঘোরা (Iteration 1):

request_count += 1 হওয়ার কারণে request_count এর মান বেড়ে হলো 1।

while request_count < 5 শর্ত চেক করা হলো। 1 তো 5 এর চেয়ে ছোট, তাই লুপের ভেতরে ঢুকল।

if is_maintenance_mode: চেক করা হলো। যেহেতু এটি True, তাই if ব্লকের ভেতরে প্রবেশ করল।

প্রিন্ট হলো: Request #1: Server is in maintenance mode. Please try again later.

ভেতরের if request_count == 3: চেক করা হলো। 1 আর 3 সমান নয়, তাই এই শর্ত মিলল না।

দ্বিতীয়বার লুপ ঘোরা (Iteration 2):

request_count += 1 হওয়ার কারণে request_count এর মান বেড়ে হলো 2।

2 < 5 শর্ত সত্য হওয়ায় লুপ আবার ঘুরল।

is_maintenance_mode এখনো True আছে।

প্রিন্ট হলো: Request #2: Server is in maintenance mode. Please try again later.

ভেতরের শর্ত (2 == 3) আবার মিলল না।

তৃতীয়বার লুপ ঘোরা (Iteration 3):

request_count += 1 হওয়ার কারণে request_count এর মান বেড়ে হলো 3।

3 < 5 শর্ত সত্য, তাই লুপ ঘুরল।

is_maintenance_mode এখনো True থাকায় প্রিন্ট হলো: Request #3: Server is in maintenance mode. Please try again later.

এবার ভেতরের শর্ত চেক করা হলো: if request_count == 3:। যেহেতু 3 এবং 3 মিলে গেছে, তাই এর ভেতরের কাজগুলো হলো:

is_maintenance_mode = False (অর্থাৎ সার্ভার মেইনটেন্যান্স থেকে লাইভ মোডে চলে গেল)।

প্রিন্ট হলো: --- Server is now live! ---

চতুর্থবার লুপ ঘোরা (Iteration 4):

request_count += 1 হওয়ার কারণে request_count এর মান বেড়ে হলো 4।

4 < 5 শর্ত সত্য, তাই লুপ ঘুরল।

if is_maintenance_mode: চেক করা হলো। কিন্তু একটু আগেই আমরা এর মান False করে দিয়েছি! তাই এটি আর if ব্লকে ঢুকবে না, সরাসরি চলে যাবে else ব্লকে।

প্রিন্ট হলো: Request #4: Successfully processed.

পঞ্চমবার লুপ ঘোরা (Iteration 5):

request_count += 1 হওয়ার কারণে request_count এর মান বেড়ে হলো 5।

while request_count < 5 শর্ত চেক করা হলো: 5 < 5 (৫ কি ৫ এর ছোট?)। না, এটি মিথ্যা বা False!

শর্ত মিথ্যা হওয়ার কারণে while লুপের কাজ এখানেই চিরতরে শেষ বা টার্মিনেট হয়ে গেল।

চূড়ান্ত আউটপুট:
সম্পূর্ণ কোডটি রান করার পর টার্মিনালে এই লেখাগুলো দেখা যাবে:

Plaintext
Request #1: Server is in maintenance mode. Please try again later.
Request #2: Server is in maintenance mode. Please try again later.
Request #3: Server is in maintenance mode. Please try again later.
--- Server is now live! ---
Request #4: Successfully processed.
