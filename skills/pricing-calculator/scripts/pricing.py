#!/usr/bin/env python3
"""Freelance quote calculator - deterministic maths, no guessing.

Usage:
    python3 pricing.py --hours 20 --rate 15 --fee 10 --rush week --revisions 3

rush: none (1.0x) | week (1.25x, due in under 7 days) | urgent (1.5x, under 48h)
Each revision round beyond 2 adds 10%.
The quote is grossed up so the freelancer keeps the target amount
after the platform fee is taken.
"""
import argparse


def main():
    p = argparse.ArgumentParser(description="Freelance pricing calculator")
    p.add_argument("--hours", type=float, required=True)
    p.add_argument("--rate", type=float, required=True, help="hourly rate in your currency")
    p.add_argument("--fee", type=float, default=0, help="platform fee percent (Upwork 10, Fiverr 20, direct 0)")
    p.add_argument("--rush", choices=["none", "week", "urgent"], default="none")
    p.add_argument("--revisions", type=int, default=2)
    a = p.parse_args()

    rush_mult = {"none": 1.0, "week": 1.25, "urgent": 1.5}[a.rush]
    rev_mult = 1.0 + max(0, a.revisions - 2) * 0.10
    base = a.hours * a.rate
    target = base * rush_mult * rev_mult
    fee_frac = a.fee / 100.0

    def quote(mult):
        q = target * mult / (1 - fee_frac) if fee_frac < 1 else target * mult
        return q, q * (1 - fee_frac)

    print(f"Base: {a.hours:g}h x {a.rate:g} = {base:.2f}")
    print(f"After rush x{rush_mult:g} and revisions x{rev_mult:.2f}: {target:.2f} (amount you must keep)")
    for label, m in [("Low", 0.85), ("Recommended", 1.0), ("High", 1.25)]:
        q, keep = quote(m)
        print(f"{label}: quote {q:.2f} -> you keep {keep:.2f} after {a.fee:g}% fee")


if __name__ == "__main__":
    main()
