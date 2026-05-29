# Reddit Niche Research

Workflow logic and idea:

In step 1 we research reddit with 4 different LLMs all with live web access - Perplexity , OpenAI chatgpt with responses API for web search , Manus AI , any other one

. We are looking for questions that a specific company type is asking about problems that they have. The goal here is to find  common problems that this niche has so we can later try to solve them.
You get the output of the llms and feed it into a new agent in step 2.

In step 2 we collect all the found questions and put them in a table. Then you show me all the questions and wait for me to choose the ones I like.
After I tell you the ones I like you run the second part of step 2.
Second part of step 2 is for every question I like to check the big data that was feeded as input to prompt 1 for something useful to me connected to the questions that I picked as liked. Then you return to me for each question the useful data and our workflow ends

For each step you can find the exact prompts and instructions below:

## Step 1 - feed this prompt to 4 different LLMs:

I am currently researching to find problems that.   **{{}}.**  companies have. I have come to the conclusion that Reddit is a very good place to find problems. My strategy was absolutely manual so far. I go into Reddit and I search for subreddits for **{{}}** owners, **{{}}** companies where they just share some common frustration. I used to search with question marks. I used to search for questions that **{{}}** companies or owners ask. That way I find some questions which have a lot of engagement, and then I put all of the questions in a table and then I check which question is potential for me to find a solution for it. Reddit, I think, is the most potential community for that operation, but if something else comes to your mind in terms of where exactly to do this, go ahead. You have all the freedom to try everything you want to try out. For me, the important thing is, at the end, to get a table of questions that **{{}}** owners ask, and then I will come up with a solution to one or more of these questions. So do deep research. Highly recommend Reddit for that. And give me the results.

## Step 2 - new ChatGpt chat to summarize all the questions from 4 LLM outputs

[https://chatgpt.com/c/69b2cfea-848c-83a0-9937-8a2a79f00283](https://chatgpt.com/c/69b2cfea-848c-83a0-9937-8a2a79f00283)

### Part one - you use Prompt 1:

I am going to give you a comparison and cleaning up of data task. I'm going to send you four different outputs of four different LLMs. All four contain quick research on questions that {{}} companies ask online, the problem that they have, and maybe some data about a potential solution or how deep the problem is. Some extra data, which is different in every output of the four. Your simple task is to get all of the questions from these four outputs and return me a plain simple table just with the questions. Below the table, specify which questions have been encountered most often across the four different responses from the llms.

**Questions:**

### Use this prompt with the questions that I pick Prompt 2:

Okay, so now I'm gonna give you the questions that I like, and I can build a solution to solve these questions. From the big data that I gave you in the first prompt, I need you to find everything connected to these questions which can be of use for me:

**Questions:**

---

---

---

---

# I TAKE OVER

## Step 3 : discuss and find solutions tot the questions with AI - new chatgpt chat

[https://chatgpt.com/c/69b3daa3-6554-839b-a0c1-a9e1d78113c8](https://chatgpt.com/c/69b3daa3-6554-839b-a0c1-a9e1d78113c8)

### Prompt 1:

Hey, I found this question in an **{{}}** community. An **{{}}** business owner has asked this question. Can you tell me what he actually meant. I'm just interested to know if I can solve this problem for this person. I want you to keep it short and simple as humanly possible. I want you to tell me what the problem is and if there is any kind of a digital system which can solve it

**Question:**

### Prompt 2:

Okay, so what we're doing now is I'm gonna send you other questions. Again, what we need to look out for is: is there a simple solution to them? A simple solution might be just a CRM or a simple scheduling system or call outreach system, some simple system which I can build for that solution. Also, you explain the problem to me.

**So, our next question is:**