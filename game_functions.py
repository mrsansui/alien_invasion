import  pygame
def update_screen(ai_settings, screen, ship, alien,bullets):

    for bullet in bullets:
        bullet.draw_bullet()
    ship.blitme()
    alien.blitme()
    pygame.display.flip()