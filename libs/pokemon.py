import pokepy

client = pokepy.V2Client()


class Pokemon:
    @staticmethod
    def pokemon(identifier):
        """mama mia i love a me some a spaghetti code"""
        global client
        pokeman = client.get_pokemon(identifier)
        return {
            'name': pokeman[0].name.title(),
            'pokedex': pokeman[0].id,
            'sprite': pokeman[0].sprites.front_default,
            'types': [str(typee.type.name).title() for typee in pokeman[0].types],
            'base_stats': [pokeman[0].stats[0].base_stat,
                           pokeman[0].stats[1].base_stat,
                           pokeman[0].stats[2].base_stat,
                           pokeman[0].stats[3].base_stat,
                           pokeman[0].stats[4].base_stat,
                           pokeman[0].stats[5].base_stat],
            'weight': str(pokeman[0].weight / 10) + ' kg',
            'height': str(pokeman[0].height / 10) + ' m',
            'abilities': [ability.ability.name.title() for ability in pokeman[0].abilities],
            'indices': [str(indice.version.name).title() for indice in pokeman[0].game_indices],

        }

    @staticmethod
    def berry(identifier):
        global client
        berri = client.get_berry(identifier)
        berri = berri[0]
        return {
            "name": berri.name,
            "id": berri.id,
            "firmness": berri.firmness.name,
            "growth-time": f"``{berri.growth_time}`` hours at sprouted, ``{berri.growth_time*2}`` hours at taller, "
                           f"``{berri.growth_time*3}`` hours at flowering, and ``{berri.growth_time*4}`` hours at "
                           f"berries!",
            "size": "``" + str(berri.size) + "`` cm",
            "smoothness": '``' + str(berri.smoothness) + '``',
            "soil-dryness": '``' + str(berri.soil_dryness) + '``',
            "flavors": "".join(
                "``" + flavor.flavor.name.title() + "`` - ``" + str(flavor.potency) + "``, " for flavor in
                berri.flavors),
            'max': berri.max_harvest,
            'natural-gift': f"``{berri.natural_gift_type.name.title()}`` - ``{berri.natural_gift_power}``"

        }

    @staticmethod
    def type(identifier):
        global client
        typ = client.get_type(identifier)
        typ = typ[0]
        value = {'name':typ.name, 'id': typ.id}
        if len(typ.damage_relations.no_damage_to) == 0:
            value['no_damage_to'] = "``None``"
        else:
            value['no_damage_to'] = "".join("``" + ty.name.title() + '``' for ty in typ.damage_relations.no_damage_to)
        if len(typ.damage_relations.no_damage_from) == 0:
            value['no_damage_from'] = "``None``"
        else:
            value['no_damage_from'] = "".join(
                "``" + ty.name.title() + '``' for ty in typ.damage_relations.no_damage_from)
        if len(typ.damage_relations.double_damage_from) == 0:
            value['double_damage_from'] = "``None``"
        else:
            value['double_damage_from'] = "".join(
                "``" + ty.name.title() + "``, " for ty in typ.damage_relations.double_damage_from)
        if len(typ.damage_relations.double_damage_to) == 0:
            value['double_damage_to'] = "``None``"
        else:
            value['double_damage_to'] = value['double_damage_from'] = "".join(
                "``" + ty.name.title() + "``, " for ty in typ.damage_relations.double_damage_to)
        if len(typ.damage_relations.half_damage_to) == 0:
            value['half_damage_to'] = "``None``"
        else:
            value['half_damage_to'] = value['half_damage_from'] = "".join(
                "``" + ty.name.title() + "``, " for ty in typ.damage_relations.half_damage_to)
        if len(typ.damage_relations.half_damage_from) == 0:
            value['half_damage_from'] = "``None``"
        else:
            value['half_damage_from'] = value['half_damage_from'] = "".join(
                "``" + ty.name.title() + "``, " for ty in typ.damage_relations.half_damage_from)
        return value


pokemon = Pokemon.pokemon
berry = Pokemon.berry
type = Pokemon.type
