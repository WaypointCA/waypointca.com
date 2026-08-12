---
title: "The Free AI Security Lab, and Where It Sits Now"
date: 2026-08-12
lastReviewed: 2026-08-12
draft: false
tags: ["AI Security", "LLM Security", "Red Teaming", "Open Source", "Training"]
categories: ["AI Security"]
summary: "The 36-week AI security lab is still free and still open. What changed is that there is now a published curriculum behind it and a practice in front of it. Here is how the three fit together."
author: "Cameron Hopkin"
---

Seven months ago I put a free AI security learning path on GitHub. It is still there, still free, still MIT licensed, and I still take pull requests.

What has changed is the context around it. Waypoint now publishes a full doctoral-level curriculum in applied AI security and assurance, and runs AI security engagements as a practice. Three things that look similar from the outside, doing genuinely different jobs. This post is mostly about telling them apart, because I have watched people pick the wrong one.

## The lab is the on-ramp

[github.com/WaypointCA/ai-security-lab](https://github.com/WaypointCA/ai-security-lab) is a self-directed path for a security person who wants hands on keyboard. It runs in phases: foundations, offensive LLM work, classical adversarial machine learning, then building out a home lab. It assumes you already think like a security practitioner and does not stop to explain why input validation matters.

It is deliberately zero cost. The AI security training market runs five to fifteen thousand dollars for material assembled from sources that are public. I did not want the price to be the reason someone competent stayed out of this field.

What the lab gives you is reps. You will run prompt injection against something you stood up yourself, poison a model and then catch it, and break a guardrail and understand why it failed. That is the part no reading list substitutes for.

What the lab does not give you is a defensible position. It will not teach you to argue that a system is safe enough in front of someone whose job is to disbelieve you.

## The curriculum is the depth

That gap is what the [applied AI security and assurance curriculum](https://waypointca.com/ai-security/curriculum/) is for. It is the same subject matter treated at research level: seven cores from mathematical foundations through adversarial machine learning, LLM and agent red teaming, secure AI engineering, and governance.

The difference is not volume. It is what you are expected to produce. The lab asks you to complete an exercise. The curriculum asks you to build a threat model that survives review, an evaluation methodology someone else can adopt, and an assurance case you can defend when it is attacked. [Core 5](https://waypointca.com/ai-security/curriculum/llm-agent-security-red-teaming/) is published complete, syllabus and all, because it is the one that carries the most weight and I would rather people judge it than take my word for it.

It is a body of knowledge, not a program you enroll in. Nobody is granting a degree here. It exists because I wanted the argument written down.

## The practice is where it gets delivered

Then there is the [AI security practice](https://waypointca.com/ai-security/), which is the part organizations actually buy. Governance and assurance on one side, red team and evaluation on the other, and private workshops when a team wants the capability in-house rather than rented.

The honest reason all three exist: the free lab is how I keep my own hands dirty, the curriculum is how I make the reasoning inspectable, and the practice is how any of it pays for itself. Each one makes the next more credible. A firm that claims AI security expertise and has published nothing you can check is asking you to take it on faith.

## Which one you want

If you are a practitioner trying to move into AI security, start with the lab. It is free and it will tell you within a few weeks whether you actually like this work.

If you are trying to understand what a serious treatment of the field requires, or you are building a program and want a defensible structure to steal from, read the curriculum. Take what is useful. That is what publishing it was for.

If you have AI in production and someone is going to ask you whether it is safe, that is an engagement, and you should probably [just talk to us](https://calendly.com/tech-waypointca/30min).

The lab is the one I would point a stranger to first. It costs nothing and it is the only one of the three that will teach you whether you have the temperament for this.
