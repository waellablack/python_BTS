def traiter_imc(imc):
    if imc < 16.0:
        print( "Maigre sévère")
    elif 16.0 <= imc < 16.9:
        print( "Maigre modéré")
    elif 17.0 <= imc < 18.4:
        print( "Maigre léger")
    elif 18.5 <= imc < 24.9:
        print( "Normal")
    elif 25.0 <= imc < 29.9:
        print( "Surpoids")
    elif 30.0 <= imc < 34.9:
        print( "Obésité modérée")
    elif 35.0 <= imc < 39.9:
        print( "Obésité sévère")
    else:
        print( "Obésité très sévère")
