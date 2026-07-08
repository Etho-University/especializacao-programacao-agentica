import dspy
from dspy.datasets import HotPotQA

lm = dspy.OpenAI(model="gpt-4o-mini")
dspy.settings.configure(lm=lm)

class RAG(dspy.Module):
    def __init__(self, num_passages=3):
        self.retrieve = dspy.Retrieve(k=num_passages)
        self.generate = dspy.ChainOfThought("context, question -> answer")

    def forward(self, question):
        context = self.retrieve(question).passages
        return self.generate(context=context, question=question)

dataset = HotPotQA(train_seed=1, train_size=20, eval_seed=1, dev_size=10)
trainset = [dspy.Example(question=q, answer=a).with_inputs("question") for q, a in zip(dataset.train["question"], dataset.train["answer"])][:5]
devset = [dspy.Example(question=q, answer=a).with_inputs("question") for q, a in zip(dataset.dev["question"], dataset.dev["answer"])][:3]

rag = RAG()
print("Antes da otimização:")
for ex in devset:
    pred = rag(question=ex.question)
    print(f"  Q: {ex.question[:50]}... -> A: {pred.answer[:50]}...")

optimizer = dspy.BootstrapFewShot(metric=dspy.evaluate.answer_exact_match)
optimized_rag = optimizer.compile(RAG(), trainset=trainset, valset=devset)

print("\nApós otimização:")
for ex in devset:
    pred = optimized_rag(question=ex.question)
    print(f"  Q: {ex.question[:50]}... -> A: {pred.answer[:50]}...")

print(f"\nCusto total estimado: {lm.total_cost:.4f}" if hasattr(lm, 'total_cost') else "\nOtimização concluída.")
