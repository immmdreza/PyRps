from src.Rps.RpsCore import RpsCore


core = RpsCore()
m = core.NewMatch

match = core.GetMatch(m)

match.AddPlayer(123456)
match.AddPlayer(654321)

match.Fight(
    {
        123456: 'dragon',
        654321: 'fire'
    }
)

print(match.PlayerStatus)
