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
  LLM works on probabilistic and not deterministic. So every time LLM runs on the same prompt, it can give different results. 3 types of consistency that can be checked:
  Structural consistency (does it skip fields), Semantic consistency (are similar tickets summarised similarly), reliability consistency (does it stay within scope)
