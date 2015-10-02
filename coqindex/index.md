<style>
hr{
    width:100%;
}
h2 code{
    color:#0ff;
}
a code{
    color:#0ff;
}
h2{
    margin-top:4em;
}
.checked{
    background-color:#020;
}
.example {
    overflow:scroll;
    display:flex;
    background-color:#205;
}
.example pre{
    margin:0;
}
.code {
    width: 380px;
    border-right: 2px solid #0ff;
}
.context {
    flex-grow: 1;
}
</style>
[`reflexivity`](#reflexivity)  
[`assumption`](#assumption)  
[`apply`](#apply)  
[`subst`](#subst)  
[`rewrite`](#rewrite)  
[`discriminate`](#discriminate)  
[`destruct`](#destruct)  
[`inversion`](#inversion)  
[`simpl`](#simpl)  
[`induction`](#induction)  
  
[Everything in one file](#all)  
  
-------------------------


##<a name=reflexivity></a>`reflexivity`##
Use `reflexivity` when your goal is to prove that something equals itself.

In this example we will prove that any term `x` of type `Set` is equal to itself. After we intro the variable we can prove the goal using `reflexivity`.

<div class=example>
<div class=code>
<pre><span class=checked>Lemma everything_is_itself:
  forall x: Set, x = x.
Proof.
  intro.</span>
  reflexivity.
Qed.
</pre>
</div>
<div class=context>
<pre>
1 subgoal
x : Set
-----------(1/1)
x = x
</pre>
</div>
</div>

**Use it when:** your goal is something like `a = a`.

##<a name=assumption></a>`assumption`##

If the thing you are trying to prove is already in your context, use `assumption` to finish the proof.

In this example we show that if we assume `p` we can prove `p`. We use `assumption` to tell Coq that our goal is already true in our context because we assumed it!

<div class=example>
<div class=code>
<pre><span class=checked>Lemma everything_implies_itself:
  forall p: Prop, p -> p.
Proof.
  intros.</span>
  assumption.
Qed.
</pre>
</div>
<div class=context>
<pre>
1 subgoal
p : Prop
H : p
-----------(1/1)
p
</pre>
</div>
</div>

**Use it when:** your goal is already in your "context" of terms you already know.

##<a name=apply></a>`apply`##

If we have a hypothesis that says that `x` implies `y`, we know that to prove `y` all we really have to do is prove `x`. We can `apply` that hypothesis to a goal of `y` to transform it into `x`.

In this example we prove modus ponens. We know that `(p -> q)` and we want to prove `q` so we can use `apply` the hypothesis to transform the goal from `q` into `p`. Then we see that `p` is already an assumption so we are done!

<div class=example>
<div class=code>
<pre><span class=checked>Lemma modus_ponens:
  forall p q : Prop, (p -> q) -> p -> q.
Proof.
  intros.</span>
  apply H.
  assumption.
Qed.
</pre>
</div>
<div class=context>
<pre>
1 subgoal
p : Prop
q : Prop
H : p -> q
H0 : p
-----------(1/1)
q
</pre>
</div>
</div>

**Use it when:** you have a hypothesis where the conclusion (on the right of the arrow) is the same as your goal.

**Advanced usage:** If we know that `x` implies `y` and we know that `x` is true, we can transfrom `x` into `y` in our context using `apply`.

In this example we prove modus ponens again. We still have our hypothesis,  
`H: p -> q`  
This time we `apply` it to a different hypothesis,  
`H0: p`  
to turn that hypothesis into `q`.

<div class=example>
<div class=code>
<pre><span class=checked>Lemma modus_ponens_again:
  forall p q : Prop, (p -> q) -> p -> q.
Proof.
  intros.</span>
  apply H in H0.
  assumption.
Qed.
</pre>
</div>
<div class=context>
<pre>
1 subgoal
p : Prop
q : Prop
H : p -> q
H0 : p
-----------(1/1)
q
</pre>
</div>
</div>


##<a name=subst></a>`subst`##

If you know that an identifier (name for something) is equal to something else, you can use `subst` to substitute the identifier for the other thing.

In this example we know that `a = b` and we want to show `b = a`. We can use `subst` to transform the `a` in the goal into a `b`, so our goal becomes `b = b`. Then we can finish the proof using `reflexivity`.

<div class=example>
<div class=code>
<pre><span class=checked>Inductive bool: Set :=
  | true
  | false.

Lemma equality_commutes:
  forall (a: bool) (b: bool), a = b -> b = a.
Proof.
  intros.
  subst.</span>
  reflexivity.
Qed.
</pre>
</div>
<div class=context>
<pre>
1 subgoal
a : bool
b : bool
H : a = b
-----------(1/1)
b = a
</pre>
</div>
</div>

**Use it when:** you want to transform an identifier into an equivalent term.

##<a name=rewrite></a>`rewrite`##

If we know two terms are equal we can transform one term into the other using `rewrite`.

While `rewrite` is similar to `subst`, it also works when both sides of the equality are terms. An identity is just a name like `x`, while a term can be more complex, like a function application: `(f x)`.

In this example we prove that if we have a function `f` and `(f x) = (f y)` then `(f y) = (f x)`. We use `rewrite` to transform `(f x)` in our goal into `(f y)` and finish the proof using `reflexivity`.

<div class=example>
<div class=code>
<pre><span class=checked>Inductive bool: Set :=
  | true
  | false.

Lemma equality_of_functions_commutes:
  forall (f: bool->bool) x y,
    (f x) = (f y) -> (f y) = (f x).
Proof.
  intros.</span>
  rewrite H.
  reflexivity.
Qed.
</pre>
</div>
<div class=context>
<pre>
1 subgoal
f : bool -> bool
x : bool
y : bool
H : f x = f y
-----------(1/1)
f y = f x
</pre>
</div>
</div>

**Use it when:** you know two terms are equivalent and you want to transform one into the other.

**Advanced usage:** you can also apply `rewrite` backwards, and to terms in your context.

**Backwards**  
If we have the hypothesis  
`H : f x = f y`  
we can change our goal from `f y` into `f x` using `rewrite` backwards:  
`rewrite <- H`

**In context**  
We can use `rewrite H1 in H2` to transform one hypothesis using a different hypothesis.

In this example we prove that equality of function application is transitive. We can use either an in-context `rewrite` or a backward `rewrite` on the goal.

<div class=example>
<div class=code>
<pre><span class=checked>Inductive bool: Set :=
  | true
  | false.

Lemma equality_of_functions_transits:
  forall (f: bool->bool) x y z,
    (f x) = (f y) ->
    (f y) = (f z) ->
    (f x) = (f z).
Proof.
  intros.</span>
  rewrite H0 in H. (* or rewrite <- H0 *)
  assumption.
Qed.
</pre>
</div>
<div class=context>
<pre>
1 subgoal
1 subgoal
f : bool -> bool
x : bool
y : bool
z : bool
H : f x = f y
H0 : f y = f z
-----------(1/1)
f x = f z
</pre>
</div>
</div>

##<a name=discriminate></a>`discriminate`##

If you have an equality in your context that isn't true, you can prove anything using `discriminate`.

For `discriminate` to work, the terms must be "structurally" different. This means that both terms are elements of an inductive set but they are built differently, using different constructors (e.g. `true` and `false`, or `(S O)` and `(S (S O))`).

In this example we show that if we assume `true = false` then we can prove anything. Note that we don't specify what `a` is, it really can be anything!

<div class=example>
<div class=code>
<pre><span class=checked>Inductive bool: Set :=
  | true
  | false.

Lemma incorrect_equality_implies_anything:
  forall a, false = true -> a.
Proof.
  intros.</span>
  discriminate.
Qed.
</pre>
</div>
<div class=context>
<pre>
1 subgoal
a : Type
H : false = true
-----------(1/1)
a
</pre>
</div>
</div>

##<a name=destruct></a>`destruct`##

We use `destruct` to perform case analysis on a term.

If we have a term of some type but we don't know what the term actually is, we can use `destruct` to examine all the possible options. It generates subgoals for each possible constructor that could have been used to construct the term. Then we prove the goal for each possibility.

In this example we show that if we negate a boolean twice, we get the same boolean back. We cannot prove this for a general `b` but we use `destruct` to prove it for any possible value of `b` (`true` or `false`).

<div class=example>
<div class=code>
<pre><span class=checked>Inductive bool: Set :=
  | true
  | false.

Definition not (b: bool) : bool :=
  match b with
    | true => false
    | false => true
  end.

Lemma not_not_x_equals_x:
  forall b, not (not b) = b.
Proof.
  intro.</span>
  destruct b.
  - reflexivity.
  - reflexivity.
Qed.
</pre>
</div>
<div class=context>
<pre>
1 subgoal
b : bool
-----------(1/1)
not (not b) = b
</pre>
</div>
</div>

##<a name=inversion></a>`inversion`##

Sometimes you have a hypothesis that can't be true unless other things are also true. We can use `inversion` to discover other necessary conditions for a hypothesis to be true.

In this example we prove that if the successors of `a` and `b` are equal then `a` and `b` are also equal. We assume that `S a = S b`. However, this can only be true if `a = b` because of how we construct `nat`s. We use `inversion` to make Coq analyze the ways it can construct `a` and `b` and it realizes that they must be equal and adds it to the context.

<div class=example>
<div class=code>
<pre><span class=checked>Inductive nat : Set :=
  | O
  | S : nat -> nat.

Lemma successors_equal_implies_equal:
  forall a b, S a = S b -> a = b.
Proof.
  intros.</span>
  inversion H.
  reflexivity.
Qed.
</pre>
</div>
<div class=context>
<pre>
1 subgoal
a : nat
b : nat
H : S a = S b
-----------(1/1)
a = b
</pre>
</div>
</div>

##<a name=simpl></a>`simpl`##

When we have a complex term we can use `simpl` to crunch it down.

In this example we prove that adding zero to any number returns the same number. We use `simpl` to "run" the `add` function in the goal. Since in the example the first argument to `add` is `O`, it simplifies the function application to just the result.

<div class=example>
<div class=code>
<pre><span class=checked>Inductive nat : Set :=
  | O
  | S : nat -> nat.

Fixpoint add (a: nat) (b: nat) : nat :=
  match a with
    | O => b
    | S x => S (add x b)
  end.

Lemma zero_plus_n_equals_n:
  forall n, (add O n) = n.
Proof.
  intros.</span>
  simpl.
  reflexivity.
Qed.
</pre>
</div>
<div class=context>
<pre>
1 subgoal
n : nat
-----------(1/1)
add O n = n
</pre>
</div>
</div>

##<a name=induction></a>`induction`##

If we want to prove a theorem using induction, we use `induction`!

When we use `induction`, Coq generates subgoals for every possible constructor of the term, similar to `destruct`. However, for inductive constructors (like `S x` for `nat`s), you also get an inductive hypothesis to help you prove your goal.

In this example we prove that adding any number to zero gives you the same number. We perform induction on `n` and get two cases.

If `n` is `O` then we know that `(add O O)` is `O` so we can use reflexivity. This is the base case.

For the inductive case we assume that the property holds for all numbers up to `n` and we have to prove it for `(S n)` (read: `n+1`).

To prove this we run the `add` function for one step using `simpl`. This brings the `S` outside the `add` function and now we can `rewrite` the goal using our inductive hypothesis. Then we use `reflexivity` to finish the proof. Good ol' `reflexivity`.

<div class=example>
<div class=code>
<pre><span class=checked>Inductive nat : Set :=
  | O
  | S : nat -> nat.

Fixpoint add (a: nat) (b: nat) : nat :=
  match a with
    | O => b
    | S x => S (add x b)
  end.

Lemma n_plus_zero_equals_n:
  forall n, (add n O) = n.
Proof.
  induction n.</span>
- reflexivity.
- simpl. rewrite IHn. reflexivity.
Qed.
</pre>
</div>
<div class=context>
<pre>
2 subgoals
-----------(1/2)
add O O = O
-----------(2/2)
add (S n) O = S n
</pre>
</div>
</div>


##<a name=all></a>All the tactics!##

Here are all examples in one file. Yay!

<pre>
(* reflexivity: use reflexivity when your goal is to prove
    that something equals itself. *)

Lemma everything_is_itself:
  forall x: Set, x = x.
Proof.
  intro.
  reflexivity.
Qed.

(* assumption: use assumption to prove a goal
    that you is already assumed in your hypotheses *)

Lemma everything_implies_itself:
  forall p: Prop, p -> p.
Proof.
  intros.
  assumption.
Qed.

(* apply: if you have the hypothesis that x implies y,
    you can apply that hypothesis to x to get y *)

Lemma modus_ponens:
  forall p q : Prop, (p -> q) -> p -> q.
Proof.
  intros.
  apply H in H0.
  assumption.
Qed.

Inductive bool: Set :=
  | true
  | false.

(* subst: if you have a hypothesis that two variables are the same
    you can use subst to substitute one for the other *)

Lemma equality_commutes:
forall (a: bool) (b: bool), a = b -> b = a.
Proof.
  intros.
  subst.
  reflexivity.
Qed.

(* rewrite: if you have a hypothesis that two expressions are equal
    you change one term into the other using rewrite *)

Lemma equality_of_functions_commutes:
  forall (f: bool->bool) x y,
    (f x) = (f y) -> (f y) = (f x).
Proof.
  intros.
  rewrite H.
  reflexivity.
Qed.

(* discriminate: if you have a equality in your context that isn't true
    you can prove anything using discriminate *)

Lemma incorrect_equality_implies_anything:
  forall a, false = true -> a.
Proof.
  intros.
  discriminate.
Qed.

Definition not (b: bool) : bool :=
  match b with
    | true => false
    | false => true
  end.

(* destruct: performs case analysis on an inductive term *)

Lemma not_not_x_equals_x:
  forall b, not (not b) = b.
Proof.
  intro.
  destruct b.
  - reflexivity.
  - reflexivity.
Qed.

Inductive nat : Set :=
  | O
  | S : nat -> nat.

(* inversion: sometimes you have a hypothesis that can't be true
    unless other things are also true. inversion add those other things
    to your context, or solve the goal if it can't *)

Lemma successors_equal_implies_equal:
  forall a b, S a = S b -> a = b.
Proof.
  intros.
  inversion H.
  reflexivity.
Qed.

Fixpoint add (a: nat) (b: nat) : nat :=
  match a with
    | O => b
    | S x => S (add x b)
  end.

(* simpl : Use simpl to crunch down a term *)

Lemma zero_plus_n_equals_n:
  forall n, (add O n) = n.
Proof.
  intros.
  simpl.
  reflexivity.
Qed.

(* induction: prove something using induction *)

Lemma n_plus_zero_equals_n:
  forall n, (add n O) = n.
Proof.
  induction n.
- simpl. reflexivity. (* Or just reflexivity *)
- simpl. rewrite IHn. reflexivity.
Qed.
</pre>

