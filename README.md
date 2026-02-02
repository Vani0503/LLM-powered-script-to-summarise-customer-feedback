# LLM-powered-script-to-summarise-customer-feedback
A tool that converts raw support tickets into structured summaries for PMs.
As a PM, I'd want the following
- Clarity (can I understand the summary in 5 seconds?)
- Structure (can I easily navigate through the summary points if there are bullet points?)
- Actionable (is there an action that is suggested that I can take as a PM?)
- Consistency across tickets
- Hallucination risk

- I find prompt 5 as the best prompt as it gives structred, bullet summary, and gives impact against each customer ticket and summarises the ticket. 
- Actionable is missing from prompts 1 and 4

- Failure cases:
  When the ticket is short, the output can be vague. When multiple issues are in one ticket, the model merges them. When sentiment is neutral, sentiment classification becomes unreliable.

- LLM works on probabilistic and not deterministic. So every time LLM runs on the same prompt, it can give different results. 3 types of consistency that can be checked:
- Structural consistency (does it skip fields), Semantic consistency (are similar tickets summarised similarly), reliability consistency (does it stay within scope)

- Added guardrail of max-Token <250 tokens to keep answers precise and enforced output format to reduce hallucination. After gaurdrails the output for prompt 5 changed a bit vs when guardrails were absent. We did becuase LLM is probabilitic, so we constrained it like a system component. 
- Adding output format enforcement will increase the likelihood of the LLM generating similar results on similar or the same prompts. Having consistency in output is important to make it production-ready for downstream consumption and APIs.
- Latency: 7.78 seconds (average response latency for a single request from client to server and back to client is 7.78 seconds which is higher than acceptable range. This will need optimisatio for real-time customer-facing use"
- Prompt tokens: 548
  Completion tokens: 250
  Total tokens: 798
  Estimated cost per request: $0.000232

- LLM sound confidential but is incorrect - model overconfidence without sufficient grounding. LLMs predict what text is most likely to come next. LLMs don't know facts; they take assumptions, do not have a real-world check, bias towards fluency.
